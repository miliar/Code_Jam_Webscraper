#include <bits/stdc++.h>
#define maxn 200005
using namespace std;

int N,tot,b[maxn],c[maxn],d[maxn],q[maxn];
map<string,int> F;
vector<int> v[205];
char s[100005];

void init()
{
	scanf("%d",&N),getchar();
	F.clear(),tot=0;
	for (int i=1; i<=N; i++)
	{
		gets(s),v[i].clear();
		string x="";
		int l=strlen(s);
		for (;l&&!isalpha(s[l-1]); l--);
		s[l++]=' ';
		for (int j=0; j<l; j++)
		{
		//	cout<<int(s[j])<<' ';
			if (isalpha(s[j])) x+=s[j];
			else
			{
			//	cout<<x<<endl;
				if (!F[x]) F[x]=++tot;
				v[i].push_back(F[x]),x="";
			}
		}
	}
}

void doit()
{
	int ans=1e9,bg=0;
//	for (int i=1; i<=N; i++){
//		for (auto j:v[i]) cout<<"  "<<j;cout<<endl;}
	memset(b,0,sizeof(b));
	memset(c,0,sizeof(c));
	memset(d,0,sizeof(d));
	for (auto i:v[1]) b[i]++;
	for (auto i:v[2])
	{
		c[i]++;
		if (c[i]&&b[i]&&!d[i]) d[i]=1,bg++;
	}
	for (int i=0; i<1<<(N-2); i++)
	{
		int s=0;
		for (int j=0; j<N-2; j++)
			for (int k:v[j+3])
			{
				if ((i>>j)&1) b[k]++; else c[k]++;
				if (b[k]&&c[k]&&!d[k]) d[k]=1,q[++s]=k;
			}
		for (int j=1; j<=s; j++) d[q[j]]=0;
		for (int j=0; j<N-2; j++)
			for (int k:v[j+3]) if ((i>>j)&1) b[k]--; else c[k]--;
		//	cout<<bg<<' '<<s+bg<<endl;
		ans=min(ans,s);
	}
	cout<<ans+bg<<endl;
}


int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int i=1; i<=T; i++)
	{
		init();
		printf("Case #%d: ",i);
		doit();
	}
	return 0;
}
