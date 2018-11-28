#include <bits/stdc++.h>

#define uint unsigned int
#define INF 999999999
#define LINF 999999999999999999
#define ll long long
#define ld long double
#define M 1000000007
#define E 0.0000001
#define N (1<<17)
#define pii pair<int, int>
#define pll pair<long long, long long>
#define pdd pair<double, double>
#define ull unsigned long long
#define C 'a'

using namespace std;

int main() {
    ifstream in("google.in");
    ofstream out("google.out");

    int t;
    in>>t;
    for (int c = 1; c <= t; c++) {
        ll n;
        in>>n;
        set<int> s;
        ll i = 0;
        while (s.size() < 10) {
            i++;
            ll tn = i * n;
            while (tn) {
                s.insert(tn % 10);
                tn /= 10;
            }
            if (i > 10000) {
                out<<"Case #"<<c<<": "<<"INSOMNIA"<<endl;
                break;
            }
        }
        if (s.size() == 10) out<<"Case #"<<c<<": "<<(i*n)<<endl;
    }
}
