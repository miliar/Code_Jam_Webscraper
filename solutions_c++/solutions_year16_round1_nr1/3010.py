#include <cstdio>
#include <vector>
#include <memory.h>
#include <string.h>
#include <tuple>
#include <list>
int main(void){
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("outputA_small.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int tc = 1; tc <= t; tc++)
	{
		std::list<char> ans;
		char str[1100];
		scanf("%s", str);
		ans.push_back(str[0]);
		for (int i = 1; str[i] != 0; i++){
			if (ans.front() > str[i]) ans.push_back(str[i]);
			else ans.push_front(str[i]);
		}
		printf("Case %d: ",tc);
		for (auto i : ans)
			printf("%c", i);
		printf("\n");
	}
}