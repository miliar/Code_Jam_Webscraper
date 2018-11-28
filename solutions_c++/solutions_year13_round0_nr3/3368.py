#include <iostream>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cstdlib>
using namespace std;

typedef long long ll;
const int maxn=10;
ll t,ans[100],limit,x;
int cnt,tot;
int a[100];
ll a1[100],b1[100];
ll aa[]={1,2,3,11,22,101,111,121,202,212,1001,1111,2002,10001,10101,10201,11011,11111,11211,20002,20102,100001,101101,110011,111111,200002,1000001,1001001,1002001,1010101,1011101,1012101,1100011,1101011,1102011,1110111,1111111,2000002,2001002};
ll bb[100];

void close()
{
exit(0);
}

bool change(ll x)
{
	memset(a,0,sizeof(a));
	cnt=0;
	while (x!=0)
	{
		cnt++;
		a[cnt]=x % 10;
		x=x/10;
	}
	for (int i=1;i<=cnt/2;i++)
		if (a[i]!=a[cnt-i+1])
			return false;
	return true;
}


void work()
{
	tot=0;
	while (x<=limit)
	{
		if (change(x))
		{
		//	printf("%I64d\n",x);
			ll t=(ll)(x*x);
			if (change(t))
			{
				tot++;
				a1[tot]=x;
				b1[tot]=t;
			//	cout<<"x:"<<x<<" t:"<<t<<endl;
				cout<<t<<",";
			}
		}
		x++;
	}
	cout<<tot<<endl;
}
//a[]={}

void init()
{

	x=1;
	limit=10000000;
	int cas;
	scanf("%d",&cas);
	for (int i=0;i<=39;i++)
		bb[i]=(ll)(aa[i])*(ll)(aa[i]);
	ll A,B;
	for (int i=1;i<=cas;i++)
	{
		printf("Case #%d: ",i);
		int ans=0;
		cin>>A>>B;
		for (int j=0;j<=39;j++)
			if (bb[j]>=A && bb[j]<=B)
				ans++;
		printf("%d\n",ans);
	}
}

int main ()
{
	init();
	close();
	return 0;
}

