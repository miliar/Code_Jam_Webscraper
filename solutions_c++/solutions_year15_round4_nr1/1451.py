#include<bits/stdc++.h>
int R,C;
char Map[100][100];
bool up_end(int r,int c)
{
	while(r>0) {r--;if(Map[r][c]!='.') return 0;}
	return 1;
}
bool down_end(int r,int c)
{
	while(r<R-1) {r++;if(Map[r][c]!='.') return 0;}
	return 1;
}
bool left_end(int r,int c)
{
	while(c>0){c--;if(Map[r][c]!='.')return 0;}
	return 1;
}
bool right_end(int r,int c)
{
	while(c<C-1) {c++;if(Map[r][c]!='.') return 0;}
	return 1;
}
int solve()
{
	int ans=0;
	for(int i=0;i<R;i++)
		for(int j=0;j<C;j++)
		{
			if(Map[i][j]=='.')continue;
			bool ok=false;
			switch(Map[i][j])
			{
				case'^':if(up_end(i,j)) ok=true;break;
				case'>':if(right_end(i,j)) ok=true;break;
				case'v':if(down_end(i,j)) ok=true;break;
				case'<':if(left_end(i,j)) ok=true;break;
			}
			if(!ok)continue;
			if(!up_end(i,j)||!right_end(i,j)||!down_end(i,j)||!left_end(i,j)) ans++;
			else return -1;
		}
	return ans;
}
int main()
{
	freopen("largeA.in","r",stdin);
	freopen("largeA.out","w",stdout);
	int T;
    scanf("%d",&T);
	int kase=0;
	while(T--)
	{
		scanf("%d%d",&R,&C);
		for(int i=0;i<R;i++)
			for(int j=0;j<C;j++)
			{
				scanf("%c",&Map[i][j]);
				bool ok=true;
				switch(Map[i][j])
				{
					case'.':
					case'^':
					case'>':
					case'v':
					case'<':break;
					default:ok=false;break;
				}
				if(!ok) j--;
			}
		int ans=solve();
		printf("Case #%d: ",++kase);
		if(ans<0)printf("IMPOSSIBLE\n");
		else printf("%d\n",ans);
	}
	return 0;
}
