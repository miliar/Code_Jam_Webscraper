//anmolarora123
#include<iostream>
#include<map>
#include<algorithm>
#include<vector>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#define f(i,a,n) for(int i=a;i<n;i++)
#define ll long long
#define si(a) scanf("%d",&a)
#define sl(a) scanf("%lld",&a)
#define ss(s) scanf("%s",s)
#define pi(a) printf("%d\n",a)
#define pl(a) printf("%lld ",a)
using namespace std;
ll to_num(char s[])
{
	ll x=0;
	int l=strlen(s);
	f(i,0,l)
	x=x*10+s[i]-'0';
	return x;
	}
int main()
{
	freopen("new.in","r",stdin);
	freopen("2.out","w",stdout);
	int t,l;
	ll n,d;
	si(t);
	char a[1000];
	char b[1000];
	char s[1000];
	ll p=pow(2,40);
	f(xxx,1,t+1)
	{
	ss(s);
	l=strlen(s);
	int i;
	for(i=0;i<l;i++)
	{
		if(s[i]=='/')
		break;
		a[i]=s[i];
		}
		a[i]=0;
		int k=0;
		for(i=i+1;i<l;i++)
		{
			b[k++]=s[i];
			}
			b[k]='\0';
	n=to_num(a);
	d=to_num(b);
	//cout<<n<<endl;
//	cout<<d<<endl;
ll c=0;
if(d%n==0)
    {
      d=d/n;
     n=1;
    }
double x;
if(p%d==0)
      {
          x=n*1.0/d;
          while(x<1.0)
           {
            x=x*2;
            c++;
           }
           
	
			printf("Case #%d: %lld\n",xxx,c);
		}
			else
			printf("Case #%d: impossible\n",xxx);
		
	
}
	return 0;
	}
