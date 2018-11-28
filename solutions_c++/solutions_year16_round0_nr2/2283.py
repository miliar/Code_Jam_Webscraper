#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <set>
#include <vector>
#include <map>

using namespace std;

char str[100010];
int main(int argc, char const *argv[])
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T = 0;
	int cas = 0;
	scanf("%d", &T);
	while(T--) {
		cas++;
		printf("Case #%d: ", cas);
		scanf("%s", str);
		int len = strlen(str);
		int cnt = 0;
		bool flip = 0;
		for(int i = len - 1; i >= 0; i--) {
			if(flip != (str[i] == '-') ) {
				cnt++;
				flip ^= 1;
			}
		}
		printf("%d\n", cnt);
		
	}
	return 0;
} 