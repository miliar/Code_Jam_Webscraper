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
	f2=fopen("outputA.txt","w");
	int t;
	fscanf(f1,"%d",&t);
	int tests=1;
	while(t--)
	{
		int r1,r2;
		int a[5][5],b[5][5];
		fscanf(f1,"%d",&r1);
		rep(i,0,3)
		 rep(j,0,3)
		  fscanf(f1,"%d",&a[i][j]);
		fscanf(f1,"%d",&r2);  
		rep(i,0,3)
		 rep(j,0,3)
		  fscanf(f1,"%d",&b[i][j]);		
		int cnt=0;
		int ans;
		rep(i,0,3)
		 rep(j,0,3)
		  if(a[r1-1][i]==b[r2-1][j])
		  {
		   ans=a[r1-1][i];	
		   cnt++;
		  }
		
		if(cnt==1)    
		 fprintf(f2,"Case #%d: %d\n",tests,ans);
		else if(cnt==0)
		 fprintf(f2,"Case #%d: Volunteer cheated!\n",tests);      
		else if(cnt>1)
		 fprintf(f2,"Case #%d: Bad magician!\n",tests); 
		tests++; 
	}
 
return 0;
}



