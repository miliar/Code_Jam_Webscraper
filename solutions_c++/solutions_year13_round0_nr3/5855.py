#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

bool check(int x)
{
    char s[105] = "";
    sprintf(s, "%d", x);
    string S = s;
    string T = S;
    reverse(S.begin(), S.end());
    return S == T;
}

int A, B;

int main()
{
	int T;  
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C.out", "w", stdout);
	scanf("%d", &T);
	for (int i = 1; i <= T; i++)
	{
        int ans = 0;
		scanf("%d%d", &A, &B);
        for (int j = 1; j <= 35; j++)
        {
            int t = j * j;
            if (check(j) && t >= A && t <= B && check(t))
                ans++;
		}
        printf("Case #%d: %d\n", i, ans);
	}
    return 0;
}

