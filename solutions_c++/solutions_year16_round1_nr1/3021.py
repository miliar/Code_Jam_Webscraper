#include <cstdio>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <string>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
using namespace std;


int main()
{
	int testcase;

	scanf("%d", &testcase);

	for(int case_number = 1; case_number <= testcase; ++case_number) {

		char s[2048];
		string ans = "";

		scanf("%s", s);

		for(int i = 0; s[i] != '\0'; ++i) {
			char c = s[i];
			if(ans + c > c + ans)
				ans = ans + c;
			else
				ans = c + ans;
		}

		printf("Case #%d: %s\n", case_number, ans.c_str());
	}

	return 0;
}
