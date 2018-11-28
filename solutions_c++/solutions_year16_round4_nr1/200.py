#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<set>
#include<map>
#include<vector>
#include<queue>
#include<functional>
#include<string>

using namespace std;

#define mp make_pair
#define pb push_back
#define fi first
#define se second

typedef long long llint;

string generate(int n,int x)
{
	if (n==0)
	{
		if (x==0) return "R";
		else if (x==1) return "P";
		else return "S";
	}
	string a = generate(n-1,x);
	string b = generate(n-1,(x+2)%3);
	if (a<b) return a+b;
	else return b+a;
}

int n,a[10],b[10],c[10];

int main()
{
	freopen("A.in","r",stdin);
	int T;
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++)
	{
		scanf("%d%d%d%d",&n,&a[0],&a[1],&a[2]);
		printf("Case #%d: ", tt);
		int i;
		for(i=0;i<3;i++)
		{
			b[0]=b[1]=b[2]=0;
			b[i]=1;
			for(int j=0;j<n;j++)
			{
				c[0]=b[0]+b[1];
				c[1]=b[1]+b[2];
				c[2]=b[2]+b[0];
				b[0]=c[0];
				b[1]=c[1];
				b[2]=c[2];
			}
			if (b[0]==a[0]&&b[1]==a[1]&&b[2]==a[2])
			{
				printf("%s\n",generate(n,i).c_str());
				break;
			}
		}
		if (i==3)
			printf("IMPOSSIBLE\n");
	}
	
	return 0;
}