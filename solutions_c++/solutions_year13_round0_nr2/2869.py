#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <utility>
#include <cstring>
#include <string>
#include <cstdio>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map<string, int> msi;

#define pb push_back
#define mp make_pair
#define S second
#define F first
#define INF 2000000000
#define MEMSET_INF 127

int l[100][100];
int maxl[100];
int maxc[100];

struct s
{
	int h;
	int x,y;
}S;

bool cmp(struct s lhs,struct s rhs)
{
	return rhs.h<lhs.h;
}

int main(int argc, char const *argv[])
{
	int t;
	int n,m;

	vector<struct s> v;
	cin>>t;

	for (int i = 0; i < t; ++i)
	{
		cin>>n>>m;

		memset(maxl,0,sizeof maxl);
		memset(maxc,0,sizeof maxc);

		for (int j = 0; j < n; ++j)
		{
			for (int k = 0; k < m; ++k)
			{
				cin>>l[j][k];
			}
		}
		for (int j = 0; j < n; ++j)
		{
			for (int k = 0; k < m; ++k)
			{
				if(l[j][k]>maxl[j])
					maxl[j]=l[j][k];
			}
		}

		for (int j = 0; j < m; ++j)
		{
			for (int k = 0; k < n; ++k)
			{
				if(l[k][j]>maxc[j])
					maxc[j]=l[k][j];
			}
		}

		int ok=1;
		for (int j = 0; j < n; ++j)
		{
			for (int k = 0; k < m; ++k)
			{
				if((l[j][k]<maxl[j])&&(l[j][k]<maxc[k]))
				{
					printf("Case #%d: NO\n",i+1);
					ok=0;
					break;
				}
			}
			if(!ok)
				break;
		}
		if(!ok)
			continue;
		printf("Case #%d: YES\n",i+1);
	}
	return 0;
}
