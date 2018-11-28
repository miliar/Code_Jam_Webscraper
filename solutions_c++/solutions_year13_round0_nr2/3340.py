#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;

const int maxn=1e2+5;
int m[maxn][maxn],maxx[maxn],maxy[maxn],a,b;

bool ok()
{
	for(int i=0;i<a;++i)
		for(int j=0;j<b;++j)
			if(maxx[i]>m[i][j] && maxy[j]>m[i][j])
				return false;
	return true;
}

int main ()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int cas;
	scanf("%d",&cas);
	for(int ii=1;ii<=cas;++ii)
	{
		scanf("%d%d",&a,&b);
		for(int i=0;i<a;++i)
			maxx[i]=0;
		for(int i=0;i<b;++i)
			maxy[i]=0;
		for(int i=0;i<a;++i)
			for(int j=0;j<b;++j)
			{
				scanf("%d",&m[i][j]);
				maxx[i]=max(maxx[i],m[i][j]);
				maxy[j]=max(maxy[j],m[i][j]);
			}
		printf("Case #%d: ",ii);
		if(ok())
			puts("YES");
		else
			puts("NO");
	}
	return 0;
}
