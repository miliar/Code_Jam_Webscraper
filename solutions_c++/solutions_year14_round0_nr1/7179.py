#include<cstdio>

inline int Read()
{
	register int c=getchar();
	int x=0;
	for(;(c<48 || c>57);c=getchar());
	for(;c>47 && c<58;c=getchar())
		x=(x<<1)+(x<<3)+c-48;
	return x;
}

int main()
{
	int t=Read();
	for(int k=0;k<t;k++)
	{
		int ar[16]={0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},cnt=0,ans;
		int ans1=Read();
		int a[4][4],b[4][4];
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
			{
				a[i][j]=Read();
				if(i==(ans1-1))
					ar[a[i][j]-1]++;
			}
		int ans2=Read();
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
			{
				b[i][j]=Read();
				if(i==(ans2-1))
				{
					if(ar[b[i][j]-1]==0)
						ar[b[i][j]-1]++;
					else
					{
						cnt++;
						ans=b[i][j];
					}
				}
			}
		if(cnt==1)
			printf("Case #%d: %d\n",k+1,ans);
		else if(cnt>1)
			printf("Case #%d: Bad magician!\n",k+1);
		else if(cnt==0)
			printf("Case #%d: Volunteer cheated!\n",k+1);
	}
	return 0;
}
