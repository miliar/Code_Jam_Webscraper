#include <bits/stdc++.h>

#define ll long long int
#define ull unsigned long long int

#define PI 2.0*acos(0.0) //#define PI acos(-1.0)
#define mem(a,val) memset(a,val,sizeof(a))

#define ptf(a) printf("%d",a)
#define nl printf("\n");

#define pb(x) push_back(x)
#define pp pop_back()
#define aov(a) a.begin(),a.end()

#define sc(a) scanf("%d",&a)
#define scm(a,b,c) scanf("%lf%lf%lf",&a,&b,&c)

#define fl(c,i,n) for(i=c;i<n;i++)
#define f(i,n) for(i=0;i<n;i++)

#define mxv(a) *max_element(aov(a))
#define mnv(a) *min_element(aov(a))

#define LB(a,x) (lower_bound(all(a),x)-a.begin())
#define UB(a,x) (upper_bound(all(a),x)-a.begin())

#define M 100000

using namespace std;


int main ()
{
//    FILE  *f2;
//    f2=fopen("out2.txt","w");


    int t,q=1;
    double c,f,x,mn,n,h,p,s;

    sc(t);
    //t=100;
    while(t--)
    {
        p=2.0;
        s=0.0;
        scm(c,f,x);
        //c=1,f=1,x=100000;

        mn=(x/p);
        while(p<=10000000)
        {
            s+=(c/p);
            p+=f;
            mn=min(mn,(x/p)+s);
        }

        printf("Case #%d: %.7lf\n",q++,mn);
    }

    return 0;
}


