#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
using namespace std;

const int NMAX=20;

struct Box
{
	int id;
	int use;
	vector<int> ins;

	bool operator<(const Box &q) const {return id<q.id;}

	void Input(int);

	void Open() const;
	void Close() const;
};

void Box::Input(int i)
{
	id=i;
	scanf("%d",&use);
	int n;
	scanf("%d",&n);
	ins.resize(n);
	for(int i=0;i<n;i++)scanf("%d",&ins[i]);
}

int N;
int has[201];
Box box[NMAX];
bool vis[1<<(NMAX-1)];

void Box::Open() const
{
	has[use]--;
	for(int i=0;i<ins.size();i++)has[ins[i]]++;
}

void Box::Close() const
{
	has[use]++;
	for(int i=0;i<ins.size();i++)has[ins[i]]--;
}

bool dfs(int mask)
{
	if(mask+1==(1<<N))return true;
	if(vis[mask])return false;
	vis[mask]=true;
	for(int i=0;i<N;i++)
	{
		if((mask&(1<<i))!=0)continue;
		if(has[box[i].use]==0)continue;
		box[i].Open();
		const bool ret=dfs(mask|(1<<i));
		box[i].Close();
		if(ret)return true;
	}
	return false;
}

bool check()
{
	memset(vis,0x00,((1<<N)-1)*sizeof(bool));
	return dfs(0);
}

void solve()
{
	while(N>0)
	{
		sort(box,box+N);
		bool flag=false;
		for(int i=0;i<N;i++)
		{
			if(has[box[i].use]==0)continue;
			//printf("[N=%d;try %d]",N,box[i].id);
			swap(box[i],box[N-1]);
			box[--N].Open();
			if(check()){flag=true;break;}
			box[N++].Close();
			swap(box[i],box[N-1]);
		}
		if(!flag){fputs(" IMPOSSIBLE",stdout);return;}
		printf(" %d",box[N].id);
	}
}

void input()
{
	memset(has,0x00,sizeof(has));
	int K;
	scanf("%d%d",&K,&N);
	while(K-->0){int k;scanf("%d",&k);has[k]++;}
	for(int i=0;i<N;i++)box[i].Input(i+1);
}

int main()
{
	int t;
	scanf("%d",&t);
	for(int s=1;s<=t;s++)
	{
		input();
		printf("Case #%d:",s);
		solve();
		putchar('\n');
	}
	return 0;
}
