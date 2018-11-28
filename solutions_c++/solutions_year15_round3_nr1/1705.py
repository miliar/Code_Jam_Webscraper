#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <utility>

using namespace std;

int main()
{
    freopen ("A-small-attempt0.in","r",stdin);
    freopen ("A-small-attempt0.out","w",stdout);

	int cas, R, C, W, ans;
	
	scanf("%d", &cas);

    for (int c = 1; c <= cas; ++c)
    {
		scanf("%d%d%d", &R, &C, &W);
		ans = (C/W + W - 1) * R;
		if (C%W != 0)
		{
			++ans;
		}
        printf("Case #%d: %d\n", c, ans);
    }

    return 0;
}