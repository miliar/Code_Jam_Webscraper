#include<cstdio>
int T,R,C;
char MAP[100][100];
bool up_end(int r,int c)
{
	while(r>0)
	{
		r--;
		if(MAP[r][c]!='.')return false; 
	}
	return true;
}
bool down_end(int r,int c)
{
	while(r<R-1)
	{
		r++;
		if(MAP[r][c]!='.')return false; 
	}
	return true;
}
bool left_end(int r,int c)
{
	while(c>0)
	{
		c--;
		if(MAP[r][c]!='.')return false; 
	}
	return true;
}
bool right_end(int r,int c)
{
	while(c<C-1)
	{
		c++;
		if(MAP[r][c]!='.')return false; 
	}
	return true;
}
int solve()
{
	int ans=0;
	for(int r=0;r<R;r++)
	{
		for(int c=0;c<C;c++)
		{
			char &v=MAP[r][c];
			if(v=='.')continue;
			bool fit=false;
			switch(v)
			{
				case'^':if(up_end(r,c))fit=true;break;
				case'>':if(right_end(r,c))fit=true;break;
				case'v':if(down_end(r,c))fit=true;break;
				case'<':if(left_end(r,c))fit=true;break;
			}
			if(!fit)continue;
			if(!up_end(r,c)||!right_end(r,c)||!down_end(r,c)||!left_end(r,c))ans++;
			else return -1;
		}
	}
	return ans;
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&T);
	int kase=1;
	while(T--)
	{
		scanf("%d%d",&R,&C);
		for(int r=0;r<R;r++)
		{
			for(int c=0;c<C;c++)
			{
				char &v=MAP[r][c];scanf("%c",&v);
				bool fit=true;
				switch(v)
				{
					case'.':
					case'^':
					case'>':
					case'v':
					case'<':break;
					default:fit=false;break;
				}
				if(!fit)c--;
			}
		}
		int ans=solve();
		printf("Case #%d: ",kase++);
		if(ans==-1)printf("IMPOSSIBLE\n");
		else printf("%d\n",ans);
	}
	return 0;
}
