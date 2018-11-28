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
{string s;
cin>>s;
lli l=s.length(),i;
for(i=l-1;i>=0;i--)
{
	if(s[i]=='-')
	break;
}
l=i+1;
if(l==0)
cout<<"Case #"<<g<<": 0\n";
else
{i=0;
lli plus=0,minu=0;
	while(1)
	{
		if(s[i]=='+')
		{plus++;
		while(i<l&&s[i]=='+')
		i++;
			}
			if(i>=l)
			break;
			if(s[i]=='-')
			{minu++;
				while(i<l&&s[i]=='-')
				i++;}
		if(i>=l)
		break;}
if(plus==0)
cout<<"Case #"<<g<<": 1\n";
else if(minu==0)
cout<<"Case #"<<g<<": 0\n";
else
{
	if(s[0]=='+')
	{cout<<"Case #"<<g<<": "<<minu*2<<"\n";
		}
		else
		{cout<<"Case #"<<g<<": "<<1+plus*2<<"\n";
			}
}
}
	
g++;}

return 0;
    }    
