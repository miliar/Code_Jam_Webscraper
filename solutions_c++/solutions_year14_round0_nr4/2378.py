#include<cstdio>
#include<vector>
#include<algorithm>
#include<cstdlib>
using namespace std;
int main()
{
	freopen("F:\\D-large.in","r",stdin);
	freopen("F:\\D-large.out","w",stdout);
	int T=0;
	double Naomi[1000];
	double Ken[1000];
	vector<double> N;
	vector<double> K;
	int n=0;
	int war_res=0;
	int d_war_res=0;
	bool flag=true;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		scanf("%d",&n);
		for(int i=0;i<n;i++)
			scanf("%lf",Naomi+i);
		for(int i=0;i<n;i++)
			scanf("%lf",Ken+i);
		sort(Naomi,Naomi+n);
		sort(Ken,Ken+n);
		N.assign(Naomi,Naomi+n);
		K.assign(Ken,Ken+n);
		/*
		for(int i=0;i<n;i++)
			printf("%lf ",N[i]);
		printf("\n");
		for(int i=0;i<n;i++)
			printf("%lf ",K[i]);
		printf("\n");
		*/
		war_res=0;
		for(int i=0;i<n;i++)
		{
			flag=false;
			for(int j=0;j<n;j++)
			{
				if(Ken[j]!=-1&&Ken[j]>Naomi[i])
				{
					Ken[j]=-1;
					flag=true;
					break;
				}
			}
			if(!flag)
			{
				for(int j=0;j<n;j++)
				{
					if(Ken[j]!=-1)
					{
						if(Ken[j]!=Naomi[i])
							war_res++;
						Ken[j]=-1;
						break;
					}
				}
			}
		}
		d_war_res=0;
		while(!N.empty())
		{
			if(N.front()>K.front())
			{
				d_war_res++;
				N.erase(N.begin());
				K.erase(K.begin());
			}
			else
			{
				N.erase(N.begin());
				K.pop_back();
			}
		}
		printf("Case #%d: %d %d\n",t,d_war_res,war_res);
		N.clear();
		K.clear();
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
