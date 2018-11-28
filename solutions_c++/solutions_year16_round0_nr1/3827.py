#include <cstdio>
#include <set>

using namespace std;

int main()
{
	int tn;
	scanf("%d", &tn);
	for(int ti = 1; ti <= tn; ++ti)
	{
		int n;
		scanf("%d", &n);
		printf("Case #%d: ", ti);
		if(n == 0) printf("INSOMNIA\n");
		else 
		{
			int ans = n;
			set<int> s;
			while(true)
			{
				int t = ans;
				while(t)
				{
					s.insert(t%10);
					t /= 10;
				}
				if(s.size() == 10) break;
				ans += n;
			}
			printf("%d\n", ans);
		}
	}
	return 0;
}

