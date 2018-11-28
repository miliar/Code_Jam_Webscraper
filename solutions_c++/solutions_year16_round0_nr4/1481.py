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


int K,C,S;

int main()
{
	int tc;
	scanf("%d",&tc);
	for (int asdf=1; asdf<=tc; asdf++)
	{
		scanf("%d %d %d",&K,&C,&S);
		if (K!=S)
		{
			printf("TODO\n");
			continue;
		}
		printf("Case #%d: ",asdf);
		for (int i=1; i<=K; i++)
			printf("%d ",i);
		printf("\n");
	}
	return 0;
}
