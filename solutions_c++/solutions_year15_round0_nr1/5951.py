#include <iostream>
#include <vector>
#include <string>

using namespace std;

int solve()
{
	int SMax = 0;
	string x;
	cin >> SMax >> x;
	int addFriends = 0;
	int StandingPeople = 0;
	for (int i = 0; i <= SMax; ++i)
	{
		StandingPeople += int(x[i] - '0');
		if (StandingPeople + addFriends < i+1)
		{
			addFriends += (i +1 - StandingPeople -addFriends);
		}
	}
	return addFriends;

}

int main()
{
	int TC = 0;
	cin >> TC;
	for (int i = 0; i < TC; ++i)
	{
		int y = solve();
		cout << "Case #" << i + 1 << ": " << y << endl;
	}
	return 0;
}
