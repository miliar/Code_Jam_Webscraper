
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~//           Author : Sarvesh Mahajan                             
//               IIIT,Hyderabad                                   
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
#define clr(x) x.clear()
#define For(i,a,b) for(i=a;i<b;i++)
#define loop(i,b) for(i=0;i<b;i++)
#define Loop(i,b) for(i=1;i<=b;i++)
#define pi(n) printf("%d ",n)
#define si(n) scanf("%d",&n)
const int MOD=1e9+7;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef long long LL;
double c,x,f;
double func(int pp)
{
double time=0.0;
double ans=2;
for(int j=0;j<pp;++j)
{
	time+=c/ans;
	ans+=f;
}

time+=x/ans;
return time;
}



int main()
{
	int n,t,m,l,k,i,j,res=0,fl;
	t=1;
	si(t);
	int T=t,pp;
	Loop(t,T)
	{
		scanf("%lf",&c);
		scanf("%lf",&f);
		scanf("%lf",&x);
		int low=0,high=x+5;
		while(high-low>=3)
		{
		           int m1=low+(high-low)/3;
			   int m2=high-(high-low)/3;
			   if(func(m1)<func(m2))
					high=m2;
				else
					low=m1;
		}

			double mini=1000000000000;

			for(j=low;j<=high;++j)
			{
				if(func(j)<mini)
				{
					mini=func(j);
//					idx=j;

				}
			}

		

			printf("Case #%d: %.7lf\n",t,mini);


		}
		return 0;
	}
