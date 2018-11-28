/*Author: Rishul Aggarwal*/

#include<bits/stdc++.h>

#define mod 1000000007
#define ll long long
#define rep(i,a,b) for(int i=a;i<=b;i++)
#define in(type,x) scanf("%" #type,&x)
#define debug(args...) {dbg,args; cerr<<endl;}
#define test int t;\
			 in(d,t);\
			 while(t--)

using namespace std;

struct debugger
{template<typename T> debugger& operator,(const T& v)
 {cerr<< v <<" ";
  return *this;
 }
}dbg;

ll gcd(ll a,ll b) {if(b==0) return a; return gcd(b,a%b);}

ll power(ll b,ll exp,ll m) {ll ans=1; b%=m; while(exp){if(exp&1) ans=(ans*b)%m; exp>>=1; b=(b*b)%m; } return ans; }

int main()
{
	FILE *f1,*f2;
	f1=fopen("input.txt","r");
	f2=fopen("outputD.txt","w");
	int t;
	fscanf(f1,"%d",&t);
	int tests=1;
	while(t--)
	{
		int n;
		double a[1002],b[1002];
		fscanf(f1,"%d",&n);
		rep(i,0,n-1)
		 fscanf(f1,"%lf",&a[i]);
		rep(i,0,n-1)
		 fscanf(f1,"%lf",&b[i]);		
	
		int ans1=0,ans2=0;
		
		sort(a,a+n),sort(b,b+n);
		
		//debug("here");
		
		bool used[1002]={0};
		rep(i,0,n-1)
		{
			bool found=0;
			rep(j,0,n-1)
			{
				if(b[j]>a[i] && used[j]==0)
				{
					found=1;
					used[j]=1; //square off this b[j] with a[i] Ken wins
					break;
				}
			}
			if(!found)
			{
				rep(j,0,n-1)
				{
					if(!used[j])
					{
						ans2++;
						used[j]=1; //square off this b[j] with a[i] Naomi wins so ans2++
						break;
					}
				}
			}
		}
		
		double maxa=a[n-1];
		//cout<<maxa<<" ";
		int last=-1;
		for(int j=n-1;j>=0;j--)
		{
		 if(b[j]<maxa)
		 {
		  last=j;	
		  break;
		 }
	    }
		
		//cout<<last;
		//debug("here");
		//debug(ans2);
		
		for(int j=last,i=n-1;i>=0 && j>=0;i--,j--)
		{
			if(a[i]>b[j])
			{
				ans1++;
				continue;
			}
			
			while(j>=0 && a[i]<b[j])
			 j--;
			
			if(j<0) break;
			
			if(a[i]>b[j])
			{
				ans1++;
				continue;
			}	  
			 
		}
				 
		fprintf(f2,"Case #%d: %d %d\n",tests,ans1,ans2);
		
		tests++; 
	}
 
return 0;
}



