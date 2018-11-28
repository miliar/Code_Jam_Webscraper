#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

const int Maxn=110;

int a[Maxn][Maxn];
int col[Maxn][Maxn],row[Maxn][Maxn];
int n,m,Test;

int Get_col(int x)
{
	int res=-1;
	for (int i=0;i<n;++i) res=max(res,a[i][x]);
	return res;
}

int Get_row(int x)
{
	int res=-1;
	for (int j=0;j<m;++j) res=max(res,a[x][j]);
	return res;
}

bool Check()
{
	int cnt=0;
	for (int i=0;i<n;++i)
		if (row[i][a[i][0]]<m)
		{
			++cnt;
			break;
		}
	if (!cnt) return true;
	cnt=0;
	for (int j=0;j<m;++j)
		if (col[j][a[0][j]]<n)
		{
			++cnt;
			break;
		}
	return (!cnt);
}

int main()
{
	freopen("B2.in","r",stdin);
	freopen("B2.out","w",stdout);

	scanf("%d",&Test);
	for (int ii=1;ii<=Test;++ii)
	{
		printf("Case #%d: ",ii);
		scanf("%d%d",&n,&m);
		memset(row,0,sizeof(row));
		memset(col,0,sizeof(col));
		for (int i=0;i<n;++i)
			for (int j=0;j<m;++j)
			{
				scanf("%d",&a[i][j]);
				++col[j][a[i][j]];
				++row[i][a[i][j]];
			}

		bool flag=Check();
		for (;!flag;)
		{
			int Min=200,t=-1;
			for (int i=0;i<n;++i)
				if (row[i][a[i][0]]==m && a[i][0]<Min)
				{
					Min=a[i][0];
					t=i;
				}
			for (int j=0;j<m;++j)
				if (col[j][a[0][j]]==n && a[0][j]<Min)
				{
					Min=a[0][j];
					t=n+j;
				}
			
			if (Min==200) break;
			
			bool mark=false;
			if (t<n)
				for (int j=0;j<m;++j)
				{
					int tmp=a[t][j];
					--row[t][a[t][j]];
					--col[j][a[t][j]];
					a[t][j]=Get_col(j);
					++row[t][a[t][j]];
					++col[j][a[t][j]];
					mark|=(tmp!=a[t][j]);
				}
			else 
				for (int i=0;i<n;++i)
				{
					int tmp=a[i][t-n];
					--row[i][a[i][t-n]];
					--col[t-n][a[i][t-n]];
					a[i][t-n]=Get_row(i);
					++row[i][a[i][t-n]];
					++col[t-n][a[i][t-n]];
					mark|=(tmp!=a[i][t-n]);
				}
			if (!mark) break;
			flag=Check();
		}

		if (!flag) printf("NO\n");
		else printf("YES\n");
	}

	return 0;
}
