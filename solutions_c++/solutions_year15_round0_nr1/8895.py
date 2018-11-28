#include <cstdio>
#include <string>
#include <cassert>
using namespace std;

int minimumFriendsNumber(string audience)
{
	int people = audience[0] - '0';
	int additionalPeopleNeeded = 0;
	for (int i = 1; i < audience.size(); ++i)
	{
		if (audience[i] != '0' && people < i)
		{
			additionalPeopleNeeded += i - people;
			people += i - people;
		}

		people += audience[i] - '0';
	}

	return additionalPeopleNeeded;
}

void testSolution()
{
	assert(minimumFriendsNumber("11111") == 0);
	assert(minimumFriendsNumber("1") == 0);
	assert(minimumFriendsNumber("09") == 1);
	assert(minimumFriendsNumber("110011") == 2);
}

//#define TEST
int main()
{
#ifdef TEST
	testSolution();
#endif
	int testCases;
	scanf("%d\n", &testCases);
	for (int i = 0; i < testCases; ++i)
	{
		char line[1001 + 5];
		gets(line);
		const string input(line);
		printf("Case #%d: %d\n", i + 1, minimumFriendsNumber(input.substr(input.find(' ', 0) + 1)));
	}

#ifdef TEST
	system("pause");
#endif
	return 0;
}