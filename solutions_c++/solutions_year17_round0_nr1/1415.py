#include <bits/stdc++.h>
#define fori(_i,_x) for (int _i = 0; _i < _x; ++_i)
#define fora(_i,_a,_b) for (int _i = _a; _i <= _b; ++_i)
#define forb(_i,_b,_a) for (int _i = _b; _i >= _a; --_i)
#define ll long long
#define inf 1000000000
#define vi vector<int>
#define vvi vector<vector<int> >
#define vl vector<long long>
#define pi pair<int,int>
#define vpi vector<pair<int,int> >
#define vpl vector<pair<long long, long long> >
#define pl pair<long long, long long>
#define fi first
#define sc second
#define pb push_back

using namespace std;

int t, k;
string s;

int main() {
    
    cin >> t;
    fora(testcase,1,t) {
        cin >> s >> k;
        int n = s.size();
        int f = 0;
        fori(i,n-k+1) {
            if (s[i] == '-') {
                ++f;
                fora(j,i,i+k-1) {
                    if (s[j] == '-') s[j] = '+';
                    else s[j] = '-';
                }
            }
        }
        bool p = true;
        fora(i,n-k+1,n-1) if (s[i] == '-') {
            p = false;
            break;
        }
        if (p) {
            cout << "Case #" << testcase << ": " << f << endl;
        } else {
            cout << "Case #" << testcase << ": IMPOSSIBLE" << endl;
        }
    }

	return 0;
}

