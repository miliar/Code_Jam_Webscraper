#include<cstdio>
#include<vector>
#include<string>
#include<algorithm>
#include<iostream>
using namespace std;
vector<string> STR[200];
vector<int> cns[200];
vector<string> ts;
int cnt[20000];
int tmain()
{
	fprintf(stderr,"xx");
	int N;
	scanf("%d ",&N);
	char buf[20000];
	for(int i=0;i<N;i++)
	{
		vector<string> nv;
		STR[i]=nv;
		vector<int> nnv;
		cns[i]=nnv;
		fgets(buf,18000,stdin);
		//printf("<");
		//puts(buf);
		//printf(">\n");
		string s="";
		for(int j=0;buf[j];j++)
		{
			if( (buf[j]<'a' || 'z'<buf[j] ) && s!="")
			{
				STR[i].push_back(s);
								ts.push_back(s);
				s="";
			}
			if('z'>= buf[j] && buf[j]>='a')
				s+=buf[j];
		}
		if(s!="")
		{
			STR[i].push_back(s);
			ts.push_back(s);
		}
	}
	//for(int i=0;i<ts.size();i++)
	//	cout<<ts[i]<<endl;
	sort(ts.begin(),ts.end());
	//for(int i=0;i<ts.size();i++)
	//	cout<<ts[i]<<endl;
	int SZ=unique(ts.begin(),ts.end())-ts.begin();
	
	for(int i=0;i<N;i++)
		for(int j=0;j<STR[i].size();j++)
		{
			//cout<<STR[i][j]<<endl;;
			cns[i].push_back(lower_bound(ts.begin(),ts.begin()+SZ,STR[i][j])-ts.begin());
		}
	int ans=987654321;
	for(int i=0;i<(1<<(N-2));i++)
	{
		for(int j=0;j<SZ;j++) cnt[j]=0;
		for(int j=0;j<cns[0].size();j++)
		{
			cnt[cns[0][j]]=1;
			//printf("%d*\n",cns[0][j]);
		}
		for(int j=0;j<cns[1].size();j++)
		{
			cnt[cns[1][j]]|=2;
		//	printf("%d^\n",cns[1][j]);
		}
		int ii=i;
		for(int k=2;k<N;k++)
		{
			int lang=1+(ii&1);
			ii>>=1;
			for(int s=0;s<cns[k].size();s++)
				cnt[cns[k][s]]|=lang;
		}
		int tot=0;
		for(int j=0;j<SZ;j++)
		{
			tot+=(cnt[j]==3);
			
		}
		ans=min(ans,tot);
	}
	return ans;
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
		printf("Case #%d: %d\n",i,tmain());
	return 0;
}