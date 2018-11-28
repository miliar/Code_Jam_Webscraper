#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<cstdlib>
using namespace std;
char in[110];
struct alp
{
	char e;
	int num;

}seq[2][110];

int main()
{
	//freopen("BBa.in","r",stdin);
	freopen("Ba.out","w",stdout);
	int t,tt,n;
	int i,j;
	int coun[2];
	char last;
	int ans;
	scanf("%d",&t);
	for(tt=1;tt<=t;++tt)
	{

		scanf("%d",&n);
		for(i=0;i<n;++i)
		{
			coun[i]=0;
			scanf("%s",in);
			last=in[0];
			seq[i][coun[i]].e=in[0];
			seq[i][coun[i]].num=1;
			for(j=1;j<strlen(in);++j)
			{
				if(in[j]==last)
				{
					seq[i][coun[i]].num++;
				}
				else
				{
					coun[i]++;
					seq[i][coun[i]].e=in[j];
					seq[i][coun[i]].num=1;
					last=in[j];
				}

			}
		}
		/*for(i=0;i<=coun[0];++i)
		{
			printf("%d %c %d\n",i,seq[0][i].e,seq[0][i].num);
		}
		printf("\n");
		for(i=0;i<=coun[1];++i)
		{
			printf("%d %c %d\n",i,seq[1][i].e,seq[1][i].num);
		}
		printf("\n");*/
		printf("Case #%d: ",tt);
		if(coun[0]!=coun[1])
			printf("Fegla Won\n");
		else
		{
			ans=0;
			for(i=0;i<=coun[0];++i)
			{
				if(seq[0][i].e!=seq[1][i].e)
				{
					ans=-1;
					break;
				}

				ans+=abs(seq[0][i].num-seq[1][i].num);
			}
			if(ans==-1)
				printf("Fegla Won\n");
			else
				printf("%d\n",ans);
		}



	}
	return 0;
}
