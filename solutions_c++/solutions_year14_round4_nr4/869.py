#include<cstdio>
#include<algorithm>
#include<iostream>
#include<set>
#include<string>
using namespace std;
int n,m;
char s[1010][110];
int ma,num;
int id[100][100];
set<string> h;

void calc()
{
	int tot=m;
	for(int i=0;i<m;i++)
		{
			h.clear();
			if (id[i][0]==0)return;
			for(int j=1;j<=id[i][0];j++)
				{
					string ss=s[id[i][j]];
					//cout<<ss<<" here"<<endl;
					for(int k=1;k<=ss.size();k++)//cout<<ss.substr(0,k)<<endl;
						if (h.count(ss.substr(0,k))==0)
							{
								tot++;
								///cout<<h.count(ss.substr(0,k))<<endl;
								h.insert(ss.substr(0,k));
								//cout<<h.count(ss.substr(0,k))<<endl;
								//cout<<ss.substr(0,k)<<endl;
							}
				}
			//cout<<"--"<<endl;
			
		}
	//cout<<"---"<<tot<<endl;
	if (tot>ma){
		ma=tot;
		num=0;
	}
	if (tot==ma)
		num++;
}

void dfs(int x)
{
	if (x==n)
		calc();
	else
		for(int i=0;i<m;i++)
			{
				id[i][++id[i][0]]=x;
				dfs(x+1);
				id[i][0]--;
			}
}

int main()
{
	freopen("ds.in","r",stdin);
	int tt;
	scanf("%d",&tt);
	for(int ii=1;ii<=tt;ii++)
		{
			scanf("%d%d\n",&n,&m);
			for(int i=0;i<n;i++)
				scanf("%s",&s[i]);
			ma=0;
			num=0;
			for(int i=0;i<m;i++)id[i][0]=0;
			dfs(0);
			printf("Case #%d: %d %d\n",ii,ma,num);
		}
	return 0;
}


