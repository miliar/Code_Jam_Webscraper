#include <bits/stdc++.h>
#define pb push_back
#define F first
#define S second
#define SZ(x) ((int)(x).size())
#define MP make_pair
using namespace std;
typedef long long ll;
typedef pair<int,int> PII;
typedef vector<int> VI;

map<string,int> mp;
int N;
VI sen[20];
char in[100000];
int ans;
int be[20];
int word[10000];
int id;

void check()
{
	for(int i=1;i<id;i++)
		word[i]=-1;
	int cnt=0;
	for(int i=0;i<N;i++)
		for(int u:sen[i])
		{
			if(word[u]==2)
				continue;
			if(word[u]==-1)
			{
				word[u]=be[i];
				continue;
			}
			if(word[u]==be[i])
				continue;
			word[u]=2;
			cnt++;
		}
	/*if(cnt==0)
	{
		for(int i=0;i<N;i++)
			printf("be[%d]=%d\n",i,be[i]);
	}*/
	ans=min(ans,cnt);
}

void C(int l)
{
	if(l==N)
	{
		check();
		return;
	}
	be[l]=0;
	C(l+1);
	be[l]=1;
	C(l+1);
}

int main()
{
	int NumberOfTestcases;
	scanf("%d",&NumberOfTestcases);
	for(int CaseNumber=1;CaseNumber<=NumberOfTestcases;CaseNumber++)
	{
		scanf("%d",&N);
		for(int i=0;i<N;i++)
			sen[i].clear();
		mp.clear();
		id=1;
		while(getchar()!='\n');
		for(int i=0;i<N;i++)
		{
			gets(in);
			char *p=strtok(in," ");
			while(p)
			{
				int tmp=mp[string(p)];
				if(tmp==0)
				{
					tmp=id++;
					mp[string(p)]=tmp;
					//word[tmp]=-1;
				}
				sen[i].pb(tmp);
				p=strtok(NULL," ");
			}	
		}
		/*for(int i=0;i<N;i++)
		{
			printf("%d:",i);
			for(int u:sen[i])
				printf(" %d",u);
			puts("");
		}*/
		ans=123456789;
		be[0]=0;
		be[1]=1;
		C(2);
		printf("Case #%d: ",CaseNumber);
		printf("%d\n",ans);
	}
	return 0;
}
