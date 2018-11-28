#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>

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


#define MAX_N 105

char s[MAX_N];

int main()
{
	int tc;
	scanf("%d",&tc);
	for (int asdf=1; asdf<=tc; asdf++)
	{
		scanf("%s",s);
		int areas=1;
		for (int i=1; s[i]; i++)
			if (s[i]!=s[i-1])
				areas++;
		if (areas&1)
		{
			if (s[0]=='+')
				areas--;
		}
		else if (s[0]=='-')
			areas--;
		printf("Case #%d: %d\n",asdf,areas);
	}
	return 0;
}
