#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii; 

#define mp make_pair
#define F first
#define S second
#define cin inf
#define cout of

const ll N = 20;
const ll M = 20;
const ll SQ = 320;
const ll INF = 1e16;
const ll MOD = 1e9+7;

struct my
{
	int r,p,s;
};

my a[N][3];

my mrg(my a,my b)
{
	return {a.r+b.r,a.p+b.p,a.s+b.s};
}

vector<int> v;

int f(int c)
{
	if (c==1) return 0;
	if (c==0) return 1;
	if (c==2) return 2;
}

void rec(int n,int x,int h)
{
	if (n==0)
	{
		v.push_back(h);
		return;
	}	
	rec(n-1,x*2,h);
	rec(n-1,x*2+1,(h-1+3)%3);
	for (int i = 0; i<(1<<(n-1)); i++)
	{
		int t1 = i+(1<<n)*x;
		int t2 = t1+(1<<(n-1));
		if (f(v[t1])>f(v[t2]))
		{
			for (int j = 0; j<(1<<(n-1)); j++)
			{
				int h1 = j+(1<<n)*x;
				int h2 = h1+(1<<(n-1));
				swap(v[h1],v[h2]);
			}
			break;
		}
		else if (f(v[t1])<f(v[t2]))
			break;
	}
}

int main()
{
	ifstream inf("input.txt");
	ofstream of("output.txt");
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	
	a[1][0] = {1,0,1};
	a[1][1] = {1,1,0};
	a[1][2] = {0,1,1};
	for (int i = 2; i<N; i++)
	{
		a[i][0] = mrg(a[i-1][0],a[i-1][2]);
		a[i][1] = mrg(a[i-1][0],a[i-1][1]);
		a[i][2] = mrg(a[i-1][1],a[i-1][2]);
	}
	int t;
	cin >> t;
	for (int h = 1; h<=t; h++)
	{
		cout << "Case #" << h << ": ";
		int n,r,p,s;
		cin >> n >> r >> p >> s;
		v.clear();
		int f = 0;
		for (int i = 0; i<3; i++)
			if (a[n][i].r==r && a[n][i].p==p && a[n][i].s==s)
			{
				rec(n,0,i);
			//	cout << i << endl;
				for (int j = 0; j<(1<<n); j++)
				{
					if (v[j]==0) cout << "R";
					if (v[j]==1) cout << "P";
					if (v[j]==2) cout << "S";
				}
				f = 1;
				break;
			}
		if (!f)
			cout << "IMPOSSIBLE";
		cout << endl;
	}

	return 0;
}


