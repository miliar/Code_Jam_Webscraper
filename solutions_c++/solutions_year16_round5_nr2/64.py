#include<bits/stdc++.h>
using namespace std;

#define sd(mark) scanf("%d",&mark)
#define ss(mark) scanf("%s",&mark)
#define sl(mark) scanf("%lld",&mark)
#define debug(mark) printf("check%d\n",mark)
#define clr(mark) memset(mark,0,sizeof(mark))
#define MP make_pair
#define PB push_back
#define F first
#define S second
#define ll long long
#define N 10000
vector<int> v[110];
bool basic[110];
bool f[110];
char s[110];
string str[10];
int cnt[10];
int p[110];
int main()
{
	// freopen("B.in","r",stdin);
	// freopen("B.out","w",stdout);
	srand(time(NULL));
	int t,n,m,i,j,k;
	sd(t);
	for(int tt=1;tt<=t;++tt)
	{
		// cerr<<tt<<'\n';
		clr(cnt);
		for(i=0;i<110;++i)
			v[i].clear();
		clr(basic);
		sd(n);
		int cnt1=0,cnt2=0;
		for(i=1;i<=n;++i)
		{
			int x;
			sd(x);
			p[i]=x;
			if(x)
				v[x].PB(i);
			else
				basic[i]=1;
		}
		ss(s);
		sd(m);
		for(i=0;i<m;++i)
			cin>>str[i];
		for(int it=1;it<=N;++it)
		{
			for(i=1;i<=n;++i)
				f[i]=basic[i];
			string cur="";
			for(i=1;i<=n;++i)
			{
				while(true)
				{
					j=rand()%n+1;
					while(j)
					{
						if(f[j])
							break;
						j=p[j];
					}
					if(f[j])
						break;
				}
				cur+=(s[j-1]);
				f[j]=0;
				for(k=0;k<v[j].size();++k)
					f[v[j][k]]=1;
			}
			bool g[6];
			clr(g);
			for(i=0;i<n;++i)
			{
				for(j=0;j<m;++j)
					if(i+(int)str[j].length() <= n)
						if(cur.substr(i,(int)str[j].length()) == str[j])
							g[j]=1;
			}
			for(i=0;i<m;++i)
				if(g[i])
					cnt[i]++;
		}
		printf("Case #%d: ",tt);
		for(i=0;i<m;++i)
			printf("%.4lf ",((double)cnt[i])/((double)N));
		printf("\n");
	}

}