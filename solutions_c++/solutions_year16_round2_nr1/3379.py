#include <iostream>
#include <fstream>
#include <vector>
#include <stack>
#include <algorithm>
#include <queue>
#include <string>
#include <cmath>
#include <cassert>
#include <map>
#include <set>
#define MOD 1e9 + 7
#define eps 1e-9
#define pb push_back
#define mp make_pair
#define ft first
#define sd second
#define sz(a) a.size()
#define loop(i, n) for(long long (i) = 0; (i) < (n) ; ++ (i))
#define pii pair<int,int>
#define pll pair<long long,long long>
#define vii vector<int>
#define vll vector<long long>  
typedef long long ll;
typedef long double ld;

using namespace std;


/*@Sergey_Miller*/

ll ddet(vector <vector <ld> > a) {
    ld det = 1;
    ll n = sz(a);
for (int i=0; i<n; ++i) {
    int k = i;
    for (int j=i+1; j<n; ++j)
        if (abs (a[j][i]) > abs (a[k][i]))
            k = j;
    if (abs(a[k][i]) < eps) {
        det = 0;
        break;
    }
    swap (a[i], a[k]);
    if (i != k)
        det = -det;
    det *= a[i][i];
    for (int j=i+1; j<n; ++j)
        a[i][j] /= a[i][i];
    for (int j=0; j<n; ++j)
        if (j != i && abs(a[j][i]) > eps)
            for (int k=i+1; k<n; ++k)
                a[j][k] -= a[i][k] * a[j][i];
    }
    return floor(det);
}

ll cdet(vector <vector <ll> > a) {
    vector <vector <ld> > b(sz(a),vector <ld> (sz(a[0])));
    loop(i,sz(a)) {
        loop(j,sz(a[i])) {
            b[i][j] = a[i][j];
        }
    }
    return ddet(b);
}



string digs[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

int fin  = 20;

string solve(string s) {
    vector <ll> words(26,0);
    loop(i,sz(s)) {
        ++words[s[i] - 'A'];
    }

    vector <vector <ll> > cntw(10,vector <ll> (26,0));
    loop(i,10) {
        loop(j,sz(digs[i])) {
            ++cntw[i][digs[i][j] - 'A'];
        }
    }

    vector <int> nums;
    loop(r,26) {
        int i = r + 5;
        loop(j,10) {
            loop(k,sz(digs[j])) {
                if((!sz(nums) || (sz(nums) && nums[sz(nums)-1] != i)) && digs[j][k] - 'A' == i) {
                    nums.pb(i);
                }
            }
        }
    }

    //cout << char('A' + nums[sz(nums)-1]) << endl;
    vector <vector <ll> > a(10, vector <ll> (10,0));
    loop(i,10) {
        loop(j,10) {
            a[i][j] = cntw[j][nums[i]];
        }
    }
    // loop(i,10) {
    //     loop(j,10) {
    //         cout << a[i][j] << " ";
    //     }
    //     cout << "   " << words[nums[i]];
    //     cout << endl;
    // }
    // cout << "OK" << endl;
    ll dt = cdet(a);
    vector <vector<ll> > b;
    ll wl[10];
    loop(i,10) {
        b = a;
        loop(j,10) {
            b[j][i] = words[nums[j]];
        }
    //     if(i == 5) {
    //           loop(i,10) {
    //     loop(j,10) {
    //         cout << b[i][j] << " ";
    //     }
    //     //cout << "   " << words[nums[i]];
    //     cout << endl;
    //}
        //}
        wl[i] = cdet(b);
        // if(i == 5) {
        //     cout << wl[i] << endl;
        //     cout << dt << endl;
        // }
    }

    // cout << endl;
    // loop(i,10) {
    //     cout << wl[i]/dt << " ";
    // }
    // cout << endl;

    string ans;
    vector <ll> ch(26,0);
    loop(i,10) {
        loop(j,wl[i]/dt) {
            ans += ('0' + i);
            loop(k,sz(digs[i])) {
                ++ch[digs[i][k] - 'A'];
            }
        }
    }
    loop(i,26) {
        assert(words[i] == ch[i]);
    }
    return ans;
}

int main () {
    ios::sync_with_stdio(false);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int n;
    cin >> n;
    loop(i,n) {
        string s;
        cin >> s;
        s = solve(s);
        cout << "Case #" << i+1 << ": " << s << endl;
    }

    // vector <vector <ll> > a(2,vector <ll> (2));
    // a[0][0] = 1;
    // a[1][1] = 2;
    // a[1][0] = 3;
    // a[0][1] = 4;
    // cout << cdet(a);
    return 0;
}

