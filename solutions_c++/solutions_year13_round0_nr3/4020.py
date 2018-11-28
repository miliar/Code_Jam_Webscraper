#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <stack>
#include <vector>

using namespace std;
/*========================================Templates=============================================*/
// datatypes
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef double db;
typedef float ft;
typedef unsigned int uint;
int gcd( int a, int b ) {  if( !b ) return a;  return gcd( b, a % b ); }


#define tests(tc) int tc;scanf("%d",&tc);while(tc--)
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORN(i,a,b,n) for(int i=(a);i<=(b);i+=n)
#define FORR(i,a,b) for(int i=(a);i>=(b);--i)
#define FORRN(i,a,b,n) for(int i=(a);i>=(b);i-=n)
#define CLEAR(arr,v)      memset(arr,v,sizeof(arr))
#define DB(x) cerr<<#x<<" : "<<x<<endl<<flush;
#define DB2(x,y) cerr<<#x<<" : "<<x<<" "<<#y<<" : "<<y<<endl<<flush;
#define DB3(x,y,z) cerr<<#x<<" : "<<x<<" "<<#y<<" : "<<y<<" "<<#z<<" : "<<z<<endl<<flush;
#define DBAR(arr,a,b) cout<<#arr<<" : ";FOR(dbar,a,b) cerr<<arr[dbar]<<" ";cerr<<endl;
#define DBAR2(arr,a,b,x,y) cout<<#arr<<endl;FOR(dbar,a,b){ FOR(dbar2,x,y)cerr<<arr[dbar][dbar2]<<" ";cerr<<endl;}
#define INF 1<<30

/*======================================Templates Ends========================*/
/* Main Code Starts from here */
char a[20],b[20],d[20];

void convert_char(ll sqx,ll sqy)
{
	int i=0,x;
	char temp;
	while(sqx>0)
	{
		a[i]=(char)(sqx%10+48);
//		cout<<"a[i] :"<<a[i]<<endl;
		sqx/=10;
		i++;
	}
	int len=strlen(a);
//	cout<<"len :"<<len<<endl;
	for(i=0;i<len/2;i++)
	{
		temp=a[i];
		a[i]=a[len-i-1];
		a[len-i-1]=temp;
	}

    i=0;
	while(sqy>0)
	{
		b[i]=(char)(sqy%10+48);
		sqy/=10;
		i++;
	}
	
	len=strlen(b);
	
	for(i=0;i<len/2;i++)
	{
		temp=b[i];
//		cout<<"temp :"<<temp;
		b[i]=b[len-i-1];
		b[len-i-1]=temp;
	}

}

void convert_char1(ll sqx)
{
	int i=0,x;
	char temp;
	while(sqx>0)
	{
		d[i]=(char)(sqx%10+48);
//		cout<<"a[i] :"<<a[i]<<endl;
		sqx/=10;
		i++;
	}
	int len=strlen(d);
//	cout<<"len :"<<len<<endl;
	for(i=0;i<len/2;i++)
	{
		temp=d[i];
		d[i]=d[len-i-1];
		d[len-i-1]=temp;
	}
}


bool check_palin(char c[20])
{
	int lena=strlen(c),flag=0;
	for(int i=0;i<lena/2;i++)
	{
		if(c[i]!=c[lena-i-1])
		{
			flag=1;
			break;
		}
	}
	if(flag==1)
	return false;
	else
	return true;
}
ll convert_num(char xx[20])
{
	ll x=1,num=0;
	int len=strlen(xx);
	for(int i=len-1;i>=0;i--)
	{
		num=num+x*(int)(xx[i]-48);
	//	cout<<num<<"  "<<xx[i]<<endl;
		x*=10;
	}
	return  num;
}



void next_palin()
{
     int flag=1,i,t,x;
     int len=strlen(a);
     for(i=0;i<len;i++)
     {
                       if(a[i]!='9')
                       {
                                    flag=0;
                                    break;
                       }
     }
     if(flag==1)
     {
                a[0]='1';
                for(i=1;i<len;i++)
                a[i]='0';
                a[len]='1';
                a[len+1]='\0';
                return ;
     }
     flag=0;
     for(i=0;i<len/2;i++)
     {
          if(a[i]<a[len-i-1])
          flag=-1;
          else if(a[i]>a[len-i-1])
          flag=1;
          a[len-i-1]=a[i];
     }
     if(flag==-1||flag==0)
     {
          t=0;
          if(len%2==0)
          x=len/2-1;
          else
          x=len/2;
          while(a[x-t]=='9')
          {
                            a[x-t]='0';
                            a[len-1-x+t]='0';
                            t++;
          }
          a[x-t]++;
          a[len-1-x+t]=a[x-t];
     }
     return;
}
          
          




main()
{
	ll t,x,y,sqx,sqy,ans=0;
	freopen("C-large-1.in", "r", stdin);
    freopen("output.txt", "w", stdout);

	int terms=0;
	tests(tc)
	{
		terms++;
		ans=0;
		a[0]='\0';
		b[0]='\0';
		d[0]='\0';
		scanf("%lld%lld",&x,&y);
		//cout<<x<<"    input     "<<y<<endl;
		sqx=(ll)sqrt(x);
		if((ll)sqx*sqx<x)
		sqx++;
		sqy=(ll)sqrt(y);
		convert_char(sqx,sqy);
		//cout<<a<<"    ab    "<<b<<endl;
		if(check_palin(a))
		{
		   ll xxxx=sqx*sqx;
		   convert_char1(xxxx);
		   bool chk=check_palin(d);
		   if(chk)
		   ans++;
		}
		//cout<<"MIDDLE ANS :"<<ans<<endl;
		while(1)
		{
			next_palin();
//			cout<<"next_palin :"<<a<<endl;
			ll num=convert_num(a);
//			cout<<"number :"<<num<<endl;
			if(num>=sqy)
			break;
			num=num*num;
			convert_char1(num);
			bool chk=check_palin(d);
			if(chk)
			ans++;
		}
		if(check_palin(b)&&sqx!=sqy)
		{
		   ll xxxx=sqy*sqy;
		   convert_char1(xxxx);
		   bool chk=check_palin(d);
		   if(chk)
		   ans++;
		}
	//	cout<<"STRING ARE :"<<a<<"   "<<b<<endl;
		printf("Case #%d: %d\n",terms,ans);
		for(int i=0;i<20;i++)
		{
			a[i]='\0';
			b[i]='\0';
			d[i]='\0';
		}
	}
}
