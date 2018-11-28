#include "set"
#include "cstdio"
#include "algorithm"
#include "cstring"
#include "queue"

#define mp make_pair

using namespace std;

int n;
int ans;
bool check(char* t) {
	for (int i = 0; i < n; ++i)
	{
		if (t[i] == '-') {
			return false;
		}
	}
	return true;
}

void flip(int x, char* s) {
	ans++;
	for (int j = 0; j < x; ++j)
	{
		s[j] = s[j] == '-'? '+':'-';
	}
	reverse(s, s+x);
}

int main(int argc, char const *argv[])
{
	int t;
	scanf("%d", &t);
	char s[100];
	for (int testcase = 0; testcase < t; ++testcase) {
		scanf("%s", s);
		n = strlen(s);
		ans = 0;
		while (!check(s)) {
			if (s[0] == '+')
			{
				int i;
				for (i = 0; i < n; ++i)
				{
					if (s[i] == '-')
					{
						break;
					}
				}
				flip(i, s);
			}
			int i;
			for (i = n-1; i >= 0; --i)
			{
				if (s[i] == '-')
				{
					break;
				}
			}
			flip(i+1, s);

			
		}
		

		printf("Case #%d: ", testcase+1);
		printf("%d\n", ans);
		
	}
	return 0;
}