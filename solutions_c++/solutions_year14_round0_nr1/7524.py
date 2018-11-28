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
#define scm(a,b) scanf("%d%d",&a,&b)

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
    FILE  *f2;

    f2=fopen("out2.txt","w");


    int t,n,i,j,x,p=1;
    bool bl[17];
    vector<int>v;

    //sc(t);
    scanf("%d",&t);
    while(t--)
    {
        mem(bl,0);
        //sc(n);
        scanf("%d",&n);
        f(i,4)
        {
            if(i+1==n)
            {
                f(j,4)
                {
                    //sc(x);
                    scanf("%d",&x);
                    bl[x]=1;
                }
            }
            else
            f(j,4)
            {
                //sc(x);
                scanf("%d",&x);
            }
        }

        //sc(n);
        scanf("%d",&n);
        f(i,4)
        {
            if(i+1==n)
            {
                f(j,4)
                {
                    //sc(x);
                    scanf("%d",&x);
                    if(bl[x]==1)
                        v.pb(x);
                }
            }
            else
            f(j,4)
            {
                //sc(x);
                scanf("%d",&x);
            }
        }

        fprintf(f2,"Case #%d: ",p++);
        j=v.size();
        if(j==0)
            fprintf(f2,"Volunteer cheated!\n");
        else if(j>1)
            fprintf(f2,"Bad magician!\n");
        else
            fprintf(f2,"%d\n",v[0]);

        v.clear();
    }


    return 0;
}
