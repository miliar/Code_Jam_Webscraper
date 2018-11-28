#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cassert>
#include <ctime>
#include <deque>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i ++)
#define ford(i, n) for (int i = int(n) - 1; i >= 0; i --)
#define mp make_pair
#define pb push_back
#define fs first
#define sc second
#define pi 3.1415926535897932384626433832795l

typedef long long ll;
typedef long double ld;

ll d[100][2][2][2];
const int kol = 30;

int main(){
#ifdef SG
    freopen ("input.txt","rt",stdin);
  freopen ("output.txt","wt",stdout);
#endif
    int t;
    cin >> t;
    forn(qqq, t){
        int a, b, k;
        cin >> a >> b >> k;
        memset(d, 0, sizeof(d));
        d[kol][0][0][0] = 1;
        ford(i, kol){
            forn(lessa, 2){
                forn(lessb, 2){
                    forn(lessk, 2){
                        if (!d[i + 1][lessa][lessb][lessk]) continue;
                        forn(teka, 2){
                            forn(tekb, 2){
                                int tekk = (tekb & teka);
                                int newa = (lessa || ((!teka) && (((1 << i) & a) != 0)));
                                int newb = (lessb || ((!tekb) && (((1 << i) & b) != 0)));
                                int newk = (lessk || ((!tekk) && (((1 << i) & k) != 0)));
                                if ((!lessa) && teka && (!(((1 << i) & a) != 0))) continue;                        
                                if ((!lessb) && tekb && (!(((1 << i) & b) != 0))) continue;
                                if ((!lessk) && tekk && (!(((1 << i) & k) != 0))) continue;
                                //if (teka == 0 && tekb == 0 && tekk == 0) 
                                //    cerr << i << ' ' << newa << ' ' << newb << ' ' << newk << endl;
                                d[i][newa][newb][newk] += d[i + 1][lessa][lessb][lessk];
                                //cout << d[i + 1][lessa][lessb][lessk] << ' ' << lessa << ' ' << lessb << ' ' << lessk << endl;
                            }
                        }
                    
                    }
                }
            } 
        }
        ll ans = d[0][1][1][1];
        cout << "Case #" << qqq + 1<< ": " << ans << endl;
    } 

    return 0;
}
