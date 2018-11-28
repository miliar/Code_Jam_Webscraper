#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<algorithm>
#include<ctime>
#include<cctype>
#include<cmath>
#include<string>
#include<cstring>
#include<stack>
#include<queue>
#include<vector>
#include<map>
#define sqr(x) ((x)*(x))
#define LL long long
#define INF 0x3f3f3f3f
#define PI 3.14159265358979
#define eps 1e-10
#define mm

using namespace std;
/*
priority_queue<double,vector<double>,greater<double> >q11,q12;
priority_queue<double> q21,q22;
*/

double a[1111],b[1111];
bool flag;

bool cmp(const double &x,const double &y)
{
    return x>y;
}

int main()
{
	#ifndef ONLINE_JUDGE
		freopen("t","r",stdin);
		freopen("t4","w",stdout);
	#endif

	int tt,n,k,s1,s2,MIN;
	scanf("%d",&tt);
	for (int t=1;t<=tt;t++)
    {
        scanf("%d",&n);
        for (int i=0;i<n;i++)
        {
            scanf("%lf",a+i);
        }
        sort(a,a+n);
        for (int i=0;i<n;i++)
        {
            scanf("%lf",b+i);
        }
        sort(b,b+n,cmp);
        s1=0;

        for (int i=0;i<n;i++)
        {
            flag=true;
            for (int j=i;j<n;j++)
            {
                if (a[j]<b[n+i-j-1])
                {
                //    printf("%.2f %.2f\n",a[j],b[n+i-j-1]);
                    flag=false;
                    break;
                }
            }
            if (flag)
            {
              //  printf("%d\n",i);
                s1=n-i;
                break;
            }
        }

        s2=0;
        for (int i=0;i<n;i++)
        {
            MIN=-1;
            for (int j=0;j<n;j++)
            {
                if (b[j]>a[i] && (MIN==-1 || b[j]<b[MIN]))
                    MIN=j;
            }

          //  printf("%d\n",MIN);

            if (MIN==-1)
            {
                s2=n-i;
                break;
            }
            else
            {
                b[MIN]=-1;
            }
        }

        printf("Case #%d: %d %d\n",t,s1,s2);
    }


	return 0;
}
