#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
char a[200];
int main()
{
//	freopen("E:B-large.in","r",stdin);

//	freopen("E:A-small-attempt0.txt","w",stdout);

	int T,len;
	scanf("%d",&T);
	for(int fuck=1;fuck<=T;fuck++)
	{
		printf("Case #%d: ",fuck);
		scanf("%s",a);
		len=strlen(a);
		int ans=0;
		for(int i=len-1;i>=0;i--)
		{
			if(a[i]=='-')
			{
				ans++;
				for(int j=i;j>=0;j--)
				{
				    if(a[j]=='+')
                    {
					a[j]='-';continue;}
					if(a[j]=='-')
					{
					a[j]='+';
					continue;}

				}
			}
		}
		printf("%d\n",ans);
	}
}

