#include <bits/stdc++.h>

#define For(i, a, b) for(int i=(a); i<(b); ++i)
#define INF 1000000000
#define MP make_pair

using namespace std;

typedef long long ll;
typedef pair <int, int> ii;

int main()
{
	//std::ios_base::sync_with_stdio(false);

	int tt, caso = 1;
	scanf("%d", &tt);

	while (tt--)
	{
		int k, c, s;
		scanf("%d %d %d", &k, &c, &s);

		printf("Case #%d: ", caso++);
		For(i, 0, k)
			printf("%d ", i+1);
		printf("\n");
	}

	return 0;
}