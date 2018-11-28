#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <set>
#include <cstring>
#include <cmath>
#include <queue>
#include <stack>

using namespace std;

#define pb push_back
#define mp make_pair
#define pq priority_queue

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;


double v[100000000];

int main()
{
   // freopen("in.txt","r",stdin);
  //  freopen("out.txt","w",stdout);
    double c,f,x;
    int tt;
    scanf("%d",&tt);
    for(int t=1;t<=tt;++t)
    {
        scanf("%lf %lf %lf",&c,&f,&x);
        printf("Case #%d: ",t);
        v[0] = 0.;
        double cps = 2.;
        double tmp = x/cps;
        int n = 1;

        while(cps <= x*10)
        {
            double aux = v[n-1];
            double div1 = c/cps;
            cps+=f;
            v[n] = aux+div1;
            tmp = min(tmp,v[n]+x/cps);
            n++;
        }
        printf("%.7lf",tmp);
        if(t!=tt) printf("\n");
    }
    return 0;
}
