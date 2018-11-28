
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>

using namespace std;

int dx[5]={0,-1,1,0,0};
int dy[5]={0,0,0,-1,1};
int a[150][150];
int n,m;

char CI[200];

bool Can(int x,int y)
{
	if (!a[x][y]) return true;
	int tx=dx[a[x][y]];
	int ty=dy[a[x][y]];
	while (true)
    {
		x+=tx;
		y+=ty;
		if (x==0 || x==n+1 || y==0 || y==m+1) return false;
		if (a[x][y]) return true;
	}
}


int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-L.out","w",stdout);
	memset(CI,0,sizeof CI);
    CI['.']=0;  CI['^']=1;  CI['v']=2;  CI['<']=3;  CI['>']=4;
    int T;
	cin>>T;
	for (int _=1;_<=T;_++)
    {
		scanf("%d%d",&n,&m);
		for (int i=1;i<=n;i++)
        {
            getchar();
            for (int j=1;j<=m;j++)
            {
                char ctmp;
                ctmp=getchar();
                a[i][j]=CI[ctmp];
            }
        }
        printf("Case #%d: ",_);
        int ans=0;
        bool kg=true;
        for (int i=1;kg&&i<=n;i++)
            for (int j=1;kg&&j<=m;j++)
            if (!Can(i,j))
            {
                bool flag=false;
                for (int k=1;k<5;k++)
                {
                    a[i][j]=k;
                    if (Can(i,j)) {flag=true;break;}
                }
                if (!flag)
                {
                    printf("IMPOSSIBLE\n");
                    kg=false;
                    break;
                }
                ans++;
            }
        if (kg) printf("%d\n",ans);
	}
	return 0;
}
