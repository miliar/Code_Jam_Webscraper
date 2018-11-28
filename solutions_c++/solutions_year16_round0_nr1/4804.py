#include<bits/stdc++.h>
using namespace std;
 
typedef long long int lli;
   
#define pc(x) putchar_unlocked(x);
#define gc() getchar_unlocked();
#define ITR(x,c) for(__typeof(c.begin()) x=c.begin();x!=c.end();x++)
#define F(i, a,b) for( i=a;i<b;i++)
#define ZERO(a) memset(a,0,sizeof(a))
#define M 1000000007
#define pi 3.14159265358
#define pb push_back 
#define sd(n) scanf("%d",&n)
#define sl(n) scanf("%lld",&n)

int main()
{freopen("A.in","r",stdin);
freopen("google.txt","w",stdout);

int g=1,t;
sl(t);
while(t--)
{lli n,i,j;
sl(n);
int arr[10];
ZERO(arr);
F(i,0,1000)
{
	lli x=n*(i+1);
	while(x)
	{
		lli a=x%10;
		x=x/10;
		arr[a]=1;}
		F(j,0,10)
		{
			if(arr[j]==0)
			break;}
			if(j==10)
			break;
}
if(i==1000)	
cout<<"Case #"<<g<<": "<<"INSOMNIA\n";
else cout<<"Case #"<<g<<": "<<n*(i+1)<<"\n";


g++;}

return 0;
    }    
