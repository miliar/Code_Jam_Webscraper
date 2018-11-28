#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;

int main()
{
	FILE *stream;
	freopen_s(&stream, "C:\\new\\B-large.in", "r", stdin);
	freopen_s(&stream, "C:\\new\\Blarge.txt", "w", stdout);
	int T;
	scanf_s("%d", &T);
	for (int i = 1; i <= T; i++)
	{
		char pan[101];
		scanf_s("%s", pan, 101);
		int N = strlen(pan);
		char temp = pan[0];
		int s = 0;
		for (int i = 0; i < N; i++)
			if (temp != pan[i]) {
				s++;
				temp = pan[i];
			}
		if (pan[N - 1] == '-') s++;
		printf("Case #%d: %d\n", i, s);
	}
	return 0;
}