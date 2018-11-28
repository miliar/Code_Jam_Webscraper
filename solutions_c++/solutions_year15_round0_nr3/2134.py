#include<cstdio>
#include<cstring>
#include<algorithm>
#define fo(i,a,b) for(int i=a;i<=b;i++)
#define fd(i,a,b) for(int i=a;i>=b;i--)
using namespace std;

const int N = int(1e6)+5;
int n , m , T , nn;
char s[N];

const int f[5][5] = {   {0,0,0,0,0},
						{0,1,2,3,4},
						{0,2,-1,4,-3},
						{0,3,-4,-1,2},
						{0,4,3,-2,-1}};

void Init()
{
	scanf("%d%d",&n,&m);
	nn = n;
	scanf("%s",s+1);
	fo(i,1,min(11,m-1))
		fo(j,1,n) s[i*n+j] = s[j];
	n = min(12,m)*n;
}

void change(int &a,int &b,int x)
{
	a = f[a][x];
	if (a < 0) b*=-1 , a*=-1;
}

void Work(int tc)
{
	int a = 1 , b = 1;
	fo(i,1,nn)
	{
		int x;
		if (s[i] == '1') x = 1;else
		if (s[i] == 'i') x = 2;else
		if (s[i] == 'j') x = 3;else
						 x = 4;
		change(a,b,x);
	}
	int aa = 1 , bb = 1;
	fo(i,1,m)
	{
		if (b == -1) bb*=-1;
		change(aa,bb,a);
	}
	if (aa != 1 || bb!=-1)
	{
		puts("NO");
		return;
	}
	
	a = 1 , b = 1;
	int geti = 0;
	fo(i,1,n)
	{
		int x;
		if (s[i] == '1') x = 1;else
		if (s[i] == 'i') x = 2;else
		if (s[i] == 'j') x = 3;else
						 x = 4;
		change(a,b,x);
		if (a == 2)
		{
			geti = i;break;
		}
	}
	if (!geti)
	{
		puts("NO");return;
	}
	
	a=1 , b=1;
	int getk=0;
	fd(i,n,1)
	{
		int x;
		if (s[i] == '1') x = 1;else
		if (s[i] == 'i') x = 2;else
		if (s[i] == 'j') x = 3;else
						 x = 4;
		change(a,b,x);
		if (a == 4)
		{
			getk = i;break;
		}
	}
	if (!getk)
	{
		puts("NO");return;
	}
	
	if (geti < getk) puts("YES");else puts("NO");
}

int main()
{
	freopen("c.in","r",stdin); freopen("c.out","w",stdout);
	
	scanf("%d",&T);
	fo(tc,1,T)
	{
		printf("Case #%d: ",tc);
		Init();
		Work(tc);
	}
	
	return 0;
}