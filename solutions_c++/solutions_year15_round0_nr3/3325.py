#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

#define all(a) (a).begin(),(a).end()
#define pb push_back
#define sz(a) ((int)(a).size())
#define mp make_pair
#define fi first
#define se second

typedef pair<int,int> pint;
typedef long long ll;
typedef vector<int> vi;


#define MAX_N 10005

int n;
char s[MAX_N];
bool got[MAX_N][3][4][2],dp[MAX_N][3][4][2];

bool f(int i, int t, int c, bool sng)
{
	if (t>2)
		return false;
	if (i==n)
		return t==2&&c==3&&!sng;
	if (got[i][t][c][sng])
		return dp[i][t][c][sng];
	got[i][t][c][sng]=true;
	bool nsng=false;
	int nc=0;
	if (s[i]=='i')
	{
		if (c==0)
			nc=1;
		else if (c==1)
			nsng=true;
		else if (c==2)
			nc=3,nsng=true;
		else
			nc=2;
	}
	else if (s[i]=='j')
	{
		if (c==0)
			nc=2;
		else if (c==1)
			nc=3;
		else if (c==2)
			nsng=true;
		else
			nsng=true,nc=1;
	}
	else
	{
		if (c==0)
			nc=3;
		else if (c==1)
			nsng=true,nc=2;
		else if (c==2)
			nc=1;
		else
			nsng=true;
	}
	if (nsng&&sng)
		nsng=false;
	else if (sng^nsng)
		nsng=true;
	bool work=f(i+1,t,nc,nsng);
	if (nc==t+1&&!nsng)
		work|=f(i+1,t+1,0,false);
	return dp[i][t][c][sng]=work;
}

int main()
{
	int tc;
	scanf("%d",&tc);
	for (int asdf=1; asdf<=tc; asdf++)
	{
		int l,x;
		scanf("%d %d",&l,&x);
		scanf("%s",s);
		n=l;
		for (int i=1; i<x; i++)
			for (int j=0; j<l; j++)
				s[n++]=s[j];
		s[n]='\0';
		for (int i=0; i<=n; i++)
			for (int j=0; j<3; j++)
				for (int k=0; k<4; k++)
					got[i][j][k][0]=got[i][j][k][1]=false;
		printf("Case #%d: %s\n",asdf,f(0,0,0,false)?"YES":"NO");
	}
	return 0;
}
