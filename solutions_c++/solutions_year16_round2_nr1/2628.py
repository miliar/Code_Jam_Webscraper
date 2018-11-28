#include <cstdio>
#include <cstring>
#include <string>
#include <vector>

using namespace std;

int a[26];

bool f(){
	for (int i = 0; i < 26; ++i)
		if (a[i] != 0) {
			fprintf(stderr, "%c:%d\n", i + 'A', a[i]);
			return true;
		}
	return false;
}

vector<string> name(10);

int tr(char ch)
{
	return ch - 'A';
}

int main() {
	int la[10];
	name[0] = "ZERO"; la[0] = 0;
	name[1] = "TWO"; la[1] = 2;
	name[2] = "EIGHT"; la[2] = 8;
	name[3] = "SIX"; la[3] = 6;
	name[4] = "THREE"; la[4] = 3;
	name[5] = "SEVEN"; la[5] = 7;
	name[6] = "FIVE"; la[6] = 5;
	name[7] = "FOUR"; la[7] = 4;
	name[8] = "ONE"; la[8] = 1;
	name[9] = "NINE"; la[9] = 9;
	int T;
	scanf("%d\n", &T);
	for (int ttt = 1; ttt <= T; ++ttt)
	{
		printf("Case #%d: ", ttt);
		fprintf(stderr, "%d\n", ttt);

		int ans[10];
		for (int i = 0; i < 10; ++i)
			ans[i] = 0;
		for (int i = 0; i < 26; ++i)
			a[i] = 0;
		char ch;
		scanf("%c", &ch);
		for (;ch != '\n';)
		{
			a[ch - 'A'] ++;
			scanf("%c", &ch);
		}

		while (f())
		{
			// int st = 0;
			for (int i = 0; i < 10; ++i)
			{
				bool flag = true;
				while (flag) {
				for (int j = 0; j < name[i].length(); ++j)
					if (a[ tr(name[i][j]) ] <= 0)
					{
						flag = false;
						break;
					}
				if (flag) {
					for (int j = 0; j < name[i].length(); ++j)
						a[ tr(name[i][j]) ] --;
					ans[la[i]] ++;
					fprintf(stderr, "%d\n", la[i]);
				}
			}
			}
		}

		for (int i = 0; i < 10; ++i)
			for (int j = 0; j < ans[i]; ++j)
				printf("%d", i);
		printf("\n");
	}
	return 0;
}