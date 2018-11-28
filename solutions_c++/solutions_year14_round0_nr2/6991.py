#include<iostream>
#include<cstdio>
#include<vector>
#include<cmath>
#include<map>
#include<set>
#include<list>
#include<string>
#include<cstring>
#include<algorithm>
using namespace std;

#define fori(i,n) for(i=0;i<n;++i)
#define forin(i,s,n) for(i=s;i<=n;++i)
#define forn(i,n) for(i=n-1;i>=0;--i)
#define forni(i,n,e) for(i=n;i>=e;--i)
#define nil NULL
#define itr iterator
#define MAX(a,  b) ((a) > (b) ? (a) : (b))
#define MIN(a,  b) ((a) < (b) ? (a) : (b))
#define ABS(X) ( (X) > 0 ? (X) : ( -(X) ) )
#define SQ(X) ( (X) * (X) )
#define pb push_back
//#define mod 1000000009
//#define getchar getchar_unlocked

typedef long int li;
typedef long long int lli;
typedef long double ld;
typedef vector<int> vi;
typedef vector<long> vli;
typedef vector<long long> vlli;
typedef pair<int,int> ii;

/*------------------------------------------------------------------------------
++++++++++++++++++++++++++++++++Source Code+++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------------------*/
//Functions and Global variables
//int gcd(int a, int b) { return (b == 0 ? a : gcd(b, a % b)); }
//double pi=2*acos(0.0);
inline void fReadInt(int &x,FILE *fp) {
	    //Change the comment in macro of getchar_unlocked
		register int c = fgetc(fp);
	    x = 0;
	    int neg = 0;
	 
	    for(; ((c<48 || c>57) && c != '-'); c = fgetc(fp));
	 
	    if(c=='-') {
	        neg = 1;
	        c = fgetc(fp);
	    }
	 
	    for(; c>47 && c<58 ; c = fgetc(fp)) {
	        x = (x<<1) + (x<<3) + c - 48;
	    }
	 
	    if(neg)
	        x = -x;
	}
	
		 inline void fReadDouble(double &x,FILE *fp) {
	    //Change the comment in macro of getchar_unlocked
		register int c = fgetc(fp);
	    x = 0.0;
	    int neg = 0;
	    int flag=0;
	    long int dx=10;
	 
	    for(; ((c<48 || c>57) && c != '-'); c = fgetc(fp));
	 
	    if(c=='-') {
	        neg = 1;
	        c = fgetc(fp);
	    }
	 
	    for(; (c>47 && c<58) || (c=='.') ; c = fgetc(fp)) {
	    	if(c=='.')
	    	{
	    		flag=1;
	    		continue;
	    	}
	    	if(flag)
	    	{
	    		x=x+((double)(c-48))/dx;
	    		dx*=10;
	    	}
	    	else
	        x = x*10 + c - 48;
	        
	    }
	 
	    if(neg)
	        x = -x;
	}
	 
//Main()
int main()
{  
	int t,i;
	double f,x,c;
	FILE *fp,*fo;
	fp=fopen("B-large.in","r");
	fo=fopen("output.in","a"); 
	//scanf("%d",&t);
	fReadInt(t,fp);
	fori(i,t)
	{
		//scanf("%lf%lf%lf",&c,&f,&x);
		fReadDouble(c,fp);
		fReadDouble(f,fp);
		fReadDouble(x,fp);
		double ans1,ans2,r,bt;
		ans1=x/2.0;
		//cout<<ans1<<endl;
		//printf("%.7lf\n",ans1);
		r=2.0;
		bt=0.0;
		while(1)
		{
			bt+=(c/r);
			r+=f;
			ans2=bt+(x/r);
			if(ans1<=ans2)
			break;
			ans1=ans2;
		}
		
		fprintf(fo,"Case #%d: %.7lf\n",(i+1),ans1);
		
	}
	fclose(fp);
	fclose(fo);
  return 0;
}


