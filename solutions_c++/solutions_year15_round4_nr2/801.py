#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef pair <int,int> ii;
int main()
{
    double eps = 0.000000000;
    freopen("C:\\Users\\dell\\Downloads\\inputb.txt","r",stdin);
    freopen("C:\\Users\\dell\\Downloads\\outputb2.txt","w",stdout);
    int tc,t;
    scanf("%d",&tc);
    for(t = 1 ; t<=tc ; t++)
    {
        double ans = 0;
        int n;
        double r1,r2,c1,c2,v,x;
        scanf("%d %lf %lf",&n,&v,&x);
        scanf("%lf %lf",&r1,&c1);
        if(n > 1)scanf("%lf %lf",&r2,&c2);
        int flag = 1;
        if(n == 1)
        {
            //printf("%lf\n",abs(c1-x));
            if(abs(c1-x) > eps) flag = 0;
            else
            {
                ans = v/r1;
            }
        }
        else
        {
            double mn,mx;
            if(abs(c1 - c2) <= eps)
            {
                if(abs(c1 - x) > eps)
                {
                    flag = 0;
                }
                else
                {
                    double r = r1 + r2;
                    ans = v/r;
                }
                goto label;
            }
            if((c1-c2) < eps)
            {
                mn = c1;
                mx = c2;
            }
            else
            {
                mn = c2;
                mx = c1;
            }

            if((x-mn) >= eps && (mx - x) >= eps)
            {
                double v2 = ((x-c1)*v)/(c2-c1);
                double v1 = ((x-c2)*v)/(c1-c2);
                double t1 = v1/r1;
                double t2 = v2/r2;
                if(t1 - t2 < eps)
                {
                    ans = t2;
                }
                else ans = t1;
            }
            else flag = 0;
        }
        label :
        // Printing Starts here for the Test Case
        printf("Case #%d: ",t);
        // Print the result of the code here
        if(flag)printf("%0.8lf",ans);
        else printf("IMPOSSIBLE");
        //Don't do anything after this.
        printf("\n");

    }
    return 0;
}


