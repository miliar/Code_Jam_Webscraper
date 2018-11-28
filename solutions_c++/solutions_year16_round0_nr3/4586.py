#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

// returns the divisor if no divsor return 0
ll getdiv(ll number) {
    if (number <= 1) return 0;
    ll i;
    for (i=2; i*i<=number; i++) {
        if (number % i == 0)
        return i;
    }
    return 0;
}


template <typename Iter>
bool next(Iter begin, Iter end)
{
    if (begin == end)      // changed all digits
    {                      // so we are back to zero
        return false;      // that was the last number
    }
    --end;
    if ((*end & 1) == 0)   // even number is treated as zero
    {
        ++*end;            // increase to one
        return true;       // still more numbers to come
    }
    else                   // odd number is treated as one
    {
        --*end;            // decrease to zero
        return next(begin, end);   // RECURSE!
    }
}


int main()
{

    ofstream out;
    ifstream in("C-small-attempt0.in");
    out.open("output.txt");

    int t;
    in >> t;
    for(int tn = 1; tn <= t; tn++){
        int n, j;
        in >> n >> j;
        string s = "1";
        for(int i = 1; i <= n-2; i++){
            s += "0";
        }
        s += "1";
        int cnt = 0;
        out << "Case #" << tn << ":" << endl;
        do{

            ll bases[9];
            for(int i = 0; i < 9; i++){
                bases[i] = strtol(s.c_str(), NULL, i+2);
            }
            int test = 1;
            ll divisors[9];
            for(int i = 0; i < 9; i++){
                divisors[i] = getdiv(bases[i]);
                if(divisors[i] == 0){
                    test = 0;
                }
            }
            if(test){
                cnt++;
                out << s << " ";
                for(int i = 0 ; i < 9; i++){
                    if(i == 8){
                        out << divisors[i] << endl;
                        continue;
                    }
                    out << divisors[i] << " ";
                }
            }

            if(cnt == j){
                goto sl;
            }

        }while(next(s.begin()+1, s.end()-1));


        sl:;

    }

    out.close();
    in.close();

    return 0;
}
