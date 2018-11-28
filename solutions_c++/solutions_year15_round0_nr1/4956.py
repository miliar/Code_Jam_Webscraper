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

int n;
char s[1005];

int main()
{
	int tc;
	scanf("%d",&tc);
	for (int x=1; x<=tc; x++)
	{
		scanf("%d",&n);
		scanf("%s",s);
		int ans=0,sum=0;
		for (int i=0; i<=n; i++)
		{
			if (s[i]!='0'&&i>sum+ans)
				ans+=i-(sum+ans);
			sum+=s[i]-'0';
		}
		printf("Case #%d: %d\n",x,ans);
	}
	return 0;
}
