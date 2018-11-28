/*
Aniket Kumar
IIITA
*/
#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <stack>
#include <queue>
#include <cmath>
#include <unistd.h>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

#define V(a) vector<a>
#define pi pair<int,int>
#define ull unsigned long long
#define ill long long
#define F(i,a,n) for(i=(a);i<(n);++i)
#define RP(i,n) F(i,0,n)
#define SUM(v, s, i) RP(i, v.size()){ s += v[i];}
#define MP(a, b) make_pair(a, b)
#define S(x) scanf("%d",&x)
#define SZ(x) (x.size())
#define PB(a) push_back(a)
#define dbug(i,size,x) F(i,0,size){cout<<x[i]<<" ";} cout<<endl
#define tin freopen("A-small-attempt0.in","r",stdin)
#define tout freopen("jam1.out","a",stdout)

int main()
{
        tin;
        tout;
        int t, i, r, j, k , v, ans, con;

        cin >> t;


        F(i, 0, t) {

                bool p[17] = {0};

                cin >> r;

                F(j , 1, 5) {
                        F(k, 1, 5) {
                        cin >> v;

                        if (j == r) {
                                p[v] = true;
                        }
                        }
                }

                 cin >> r;
                 con = 0;

                F(j , 1, 5) {
                        F(k, 1, 5) {
                        cin >> v;

                        if (j == r && p[v] == true) {
                                ans = v;
                                con++;
                        }
                        }
                }

                printf("Case #%d: ", i + 1);

                if (con == 0) {
                        cout << "Volunteer cheated!\n";
                } else if (con == 1) {
                        cout << ans<<endl ;
                } else {
                        cout << "Bad magician!\n";
                }

        }
        return 0;
}




