#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>

long long absll(long long n){
    return n >= 0 ? n : -n;
    }

struct diff {
    long long a, b;
    std::string ssa, ssb;

    diff(long long aa, long long bb){
        a = aa;
        b = bb;
        }

    diff(const std::string &sa, const std::string &sb){
        ssa = sa;
        ssb = sb;
        sscanf(sa.c_str(), "%I64d", &a);
        sscanf(sb.c_str(), "%I64d", &b);
        }

    bool operator < (const diff & that) const{
        return absll(a-b) < absll(that.a-that.b) ||
            absll(a-b) == absll(that.a-that.b) && a < that.a ||
            absll(a-b) == absll(that.a-that.b) && a == that.a && b < that.b;
        }

    void opt(const std::string &sa, const std::string &sb){
        diff that(sa, sb);
        if (that < *this)
            *this = that;
        }
    };

void maximize(std::string::iterator from, std::string::iterator to){
    while(from != to){
        if (*from == '?')
            *from = '9';
        ++from;
        }
    }

void minimize(std::string::iterator from, std::string::iterator to){
    while(from != to){
        if (*from == '?')
            *from = '0';
        ++from;
        }
    }

int main()
{
    int tc;
    std::cin >> tc;
    for(int tn = 1; tn <= tc; tn++){
        diff dmin(0, ~(1LL<<63));
        std::string a0, b0, a, b;
        std::cin >> a0 >> b0;
        int len = a0.size();
        int i;
        for(i = 0; i < len; i++){
            if(a0[i] == '?' && b0[i] == '?'){
                a0[i] = '0'; b0[i] = '1';
                a = a0; b = b0;
                maximize(a.begin()+i, a.end()); minimize(b.begin()+i, b.end());
                dmin.opt(a, b);
                a0[i] = '1'; b0[i] = '0';
                a = a0; b = b0;
                minimize(a.begin()+i, a.end()); maximize(b.begin()+i, b.end());
                dmin.opt(a, b);
                a0[i] = '0'; b0[i] = '0';
                }
            else if(a0[i] == '?'){
                if (b0[i] > '0'){
                    a0[i] = b0[i] - 1;
                    a = a0; b = b0;
                    maximize(a.begin()+i, a.end()); minimize(b.begin()+i, b.end());
                    dmin.opt(a, b);
                    }
                if (b0[i] < '9'){
                    a0[i] = b0[i] + 1;
                    a = a0; b = b0;
                    minimize(a.begin()+i, a.end()); maximize(b.begin()+i, b.end());
                    dmin.opt(a, b);
                    }
                a0[i] = b0[i];
                }
            else if(b0[i] == '?'){
                if (a0[i] < '9'){
                    b0[i] = a0[i] + 1;
                    a = a0; b = b0;
                    maximize(a.begin()+i, a.end()); minimize(b.begin()+i, b.end());
                    dmin.opt(a, b);
                    }
                if (a0[i] > '0'){
                    b0[i] = a0[i] - 1;
                    a = a0; b = b0;
                    minimize(a.begin()+i, a.end()); maximize(b.begin()+i, b.end());
                    dmin.opt(a, b);
                    }
                b0[i] = a0[i];
                }
            else{
                if (a0[i] < b0[i]){
                    a = a0; b = b0;
                    maximize(a.begin()+i, a.end()); minimize(b.begin()+i, b.end());
                    dmin.opt(a, b);
                    break;
                    }
                if (a0[i] > b0[i]){
                    a = a0; b = b0;
                    minimize(a.begin()+i, a.end()); maximize(b.begin()+i, b.end());
                    dmin.opt(a, b);
                    break;
                    }
                }
            }
        if (i==len)
            dmin.opt(a0, b0);

        std::cout << "Case #" << tn << ": " << dmin.ssa << " " << dmin.ssb << std::endl;
        }
    return 0;
}
