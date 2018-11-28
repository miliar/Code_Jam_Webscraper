#include <cstdio>
#include <cstring>
#include <deque>
using namespace std;

int main()
{
	int T, length, count = 0;
	char str[1010];
	scanf("%d", &T);
	deque<int> dq;
	deque<int>::iterator it;
	while (T--)
	{
		dq.clear();
		scanf("%s", str);
		length = strlen(str);
		printf("Case #%d: ", ++count);

		dq.push_back(*str);
		for (int i = 1; i < length; ++i)
		{
			if (str[i] >= dq.front()) dq.push_front(str[i]);
			else dq.push_back(str[i]);
		}
		for (it = dq.begin(); it != dq.end(); ++it)
		{
			putchar(*it);
		}
		putchar('\n');
	}
	return 0;
}