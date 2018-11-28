#include <cstdio>
#include <algorithm>
#include <cstring>
#include <list>
using namespace std;

int T;
char str[1005];
list<char> laststr;
int main(void){
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	fgets(str, sizeof(str), stdin);
	for (int t = 1; t <= T; t++)
	{
		laststr.clear();
		fgets(str, sizeof(str), stdin);
		int len = strlen(str);
		printf("Case #%d: ", t);
		laststr.push_back(str[0]);
		for (int i = 1; i < len; i++)
		{
			if (str[i] == '\n' || str[i] == '\0')
				break;
			char first = laststr.front();
			if (str[i] >= first)
				laststr.push_front(str[i]);
			else
				laststr.push_back(str[i]);
		}
		for (auto iter = laststr.begin(); iter != laststr.end(); ++iter)
			putchar(*iter);
		if (t != T)
			putchar('\n');
		
	}

}