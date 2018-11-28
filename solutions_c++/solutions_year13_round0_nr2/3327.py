#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

#define N 100

int n,m;
int a[N][N];

void init()
{
	scanf("%d%d",&n,&m);
	for(int i=0;i<n;i++)
		for(int j=0;j<m;j++) scanf("%d",&a[i][j]);
}

bool hor(int i,int k)
{
	for(int j=0;j<m;j++) if(a[i][j]>k) return false;
	return true;
}

bool ver(int j,int k)
{
	for(int i=0;i<n;i++) if(a[i][j]>k) return false;
	return true;
}

bool OK()
{
	bool h,v;
	for(int i=0;i<n;i++)
		for(int j=0;j<m;j++)
		{
			if(!hor(i,a[i][j]) && !ver(j,a[i][j]))
				return false;
		}
	return true;
}

int main()
{
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
		init(); 
		printf("Case #%d: ",i+1);
		if(OK()) printf("YES\n");
		else printf("NO\n");
	}
	return 0;
}
