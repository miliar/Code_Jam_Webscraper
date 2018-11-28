#include <cstdio>
#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <bitset>
#include <numeric>
#include <climits>
#include <cfloat>
#include <functional>
using namespace std;

class Bigint
{
    static const long long MAX = 1000000000LL;
    vector<long long> a;
    bool sign;
public:
    Bigint(){
        sign = true;
    }
    Bigint(long long x){
        if(x < 0){
            sign = false;
            x *= -1;
        }else
            sign = true;
        while(x > 0){
            a.push_back(x % MAX);
            x /= MAX;
        }
    }
    Bigint(const string& s){
        sign = true;
        long long tmp = MAX;
        for(int i=s.size()-1; i>=0; --i){
            if(tmp == MAX){
                a.push_back(0);
                tmp = 1;
            }
            if('0' <= s[i] && s[i] <= '9'){
                a.back() += (s[i] - '0') * tmp;
                tmp *= 10;
            }else
                sign = false;
        }
    }
    long long getNum(){
        long long ret = 0;
        for(int i=a.size()-1; i>=0; --i){
            ret *= MAX;
            ret += a[i];
        }
        return ret * (sign? 1:-1);
    }
    string getStr() const{
        ostringstream oss;
        if(!sign)
            oss << '-';
        for(int i=a.size()-1; i>=0; --i){
            oss << a[i];
            oss << setw(9) << setfill('0');
        }
        return oss.str();
    }
    Bigint operator+(const Bigint& x) const{
        if(sign ^ x.sign){
            Bigint tmp = x;
            tmp.sign = !tmp.sign;
            return *this - tmp;
        }
        Bigint ret;
        ret.sign = sign;
        long long carry = 0;
        unsigned i = 0;
        while(i < a.size() || i < x.a.size() || carry > 0){
            if(i < a.size())
                carry += a[i];
            if(i < x.a.size())
                carry += x.a[i];
            ret.a.push_back(carry % MAX);
            carry /= MAX;
            ++ i;
        }
        return ret;
    }
    Bigint operator-(const Bigint& x) const{
        if(sign ^ x.sign){
            Bigint tmp = x;
            tmp.sign = !tmp.sign;
            return *this + tmp;
        }
        Bigint ret;
        long long carry = 0;
        unsigned i=0;
        while(i < a.size() || i < x.a.size()){
            if(i < a.size())
                carry += a[i];
            if(i < x.a.size())
                carry -= x.a[i];
            if(carry < 0){
                ret.a.push_back(MAX + carry);
                carry = -1;
            }else{
                ret.a.push_back(carry);
                carry = 0;
            }
            ++ i;
        }
        if(carry == -1){
            ret.sign = !ret.sign;
            for(unsigned j=0; j<ret.a.size(); ++j)
                ret.a[j] = MAX - ret.a[j] - 1;
            ++ ret.a[0];
        }
        while(ret.a.size() > 0 && ret.a.back() == 0)
            ret.a.pop_back();
        return ret;
    }
    Bigint operator*(const Bigint& x) const{
        if(a.size() == 0 || x.a.size() == 0)
            return 0;
        Bigint ret;
        ret.sign = !(sign ^ x.sign);
        ret.a.assign(a.size() + x.a.size(), 0);
        for(unsigned i=0; i<a.size(); ++i){
            for(unsigned j=0; j<x.a.size(); ++j){
                ret.a[i+j] += a[i] * x.a[j];
                ret.a[i+j+1] += ret.a[i+j] / MAX;
                ret.a[i+j] %= MAX;
            }
        }
        if(ret.a.size() > 0 && ret.a.back() == 0)
            ret.a.pop_back();
        return ret;
    }
    bool operator<(const Bigint& x) const{
        if(sign ^ x.sign)
            return x.sign;
        if(a.size() != x.a.size())
            return !(sign ^ (a.size() < x.a.size()));
        for(int i=a.size()-1; i>=0; --i){
            if(a[i] != x.a[i])
                return !(sign ^ (a[i] < x.a[i]));
        }
        return false;
    }
    bool operator<=(const Bigint& x) const{
        return !(x < *this);
    }
};

const Bigint MAX('1' + string(100, '0'));

bool isPalindrome(Bigint x)
{
    string s = x.getStr();
    reverse(s.begin(), s.end());
    return s == x.getStr();
}

vector<Bigint> fairSquare;

void solve(string s)
{
    for(int i=-1; i<=2; ++i){
        string t = s;
        reverse(t.begin(), t.end());
        if(i == -1)
            t = s + t;
        else
            t = s + (char)(i+'0') + t;

        Bigint x(t);
        x = x * x;
        if(MAX < x)
            return;
        
        if(isPalindrome(x))
            fairSquare.push_back(x);
    }

    solve(s + '0');
    if(count(s.begin(), s.end(), '1') < 4)
        solve(s + '1');
}

int main()
{
    fairSquare.push_back(1);
    fairSquare.push_back(4);
    fairSquare.push_back(9);
    solve("1");
    solve("2");
    sort(fairSquare.begin(), fairSquare.end());

    int n;
    cin >> n;

    for(int i=1; i<=n; ++i){
        string s, t;
        cin >> s >> t;

        Bigint a(s);
        Bigint b(t);

        int ret = upper_bound(fairSquare.begin(), fairSquare.end(), b) - lower_bound(fairSquare.begin(), fairSquare.end(), a);

        cout << "Case #" << i << ": " << ret << endl;
    }

    return 0;
}