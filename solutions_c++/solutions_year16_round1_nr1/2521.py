#include <cstdio>
#include <string>
using namespace std;

// String
char str[1002];

// Main
int main(void)
{
	int tc, cs;
	string ans;

	// Read Input
	scanf("%d", &tc);
	for(cs = 1; cs <= tc; cs++){
		printf("Case #%d: ", cs);
		scanf("%s", str);
		ans = "";
		ans += str[0];
		for(int i = 1; str[i] != '\0'; i++){
			if(str[i] < ans[0]) ans += str[i];
			else ans.insert(0, 1, str[i]);
		}
		printf("%s\n", ans.c_str());
	}

	return 0;
}
