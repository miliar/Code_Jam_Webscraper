#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int MAXN = 105;

char S[MAXN];
int N;

void Work(int Case)
{
	printf("Case #%d: ", Case);
	scanf("%s", S + 1);
	N = strlen(S + 1);
	int c = 0;
	for(int i = 1;i <= N;)
	{
		int k = i;
		for(;k <= N && S[k] == S[i];k ++);
		i = k;
		++ c;
	}
	c --;
	if (S[N] == '-') ++ c;
	printf("%d\n", c);
}

int main()
{
	//freopen("data.in","r",stdin),freopen("data.out","w",stdout);
	int T;
	scanf("%d", &T);
	for(int i = 1;i <= T;i ++) Work(i);
	return 0;
}
