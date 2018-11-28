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
#define tin freopen("B-large.in","r",stdin)
#define tout freopen("jam22.out","a",stdout)

bool check(double r,double c,double f,double x);

int main()
{
        tin;
        tout;
        int t, i;

        double c, f, x, tmp, r, tim, tmin;

        cin >>t ;

        F(i, 0, t) {
                r = 2.0;
                cin >> c >> f >> x;

                tim = 0;

                tmin = x / r;

                while (check(r, c, f, x)) {
                        tim += (c / r);
                        r += f;

                        tmp = tim + (x / r);
                     //   cout << "\n" << tmp ;

                        if (tmp < tmin) {

                                tmin = tmp;
                        }


                }

                printf("Case #%d: %.7lf\n",i + 1, tmin );

        }

        return 0;
}

bool check(double r,double c,double f,double x)
 {
        double tt, tu;

        tt = (x / r);

        tu = (c / r) + (x / (r + f));

        return (tu < tt) ;


}



