#include <string>
#include <vector>
#include <algorithm>
#include <numeric>
#include <iostream>

using namespace std;

class StandingOvation 
{
public:
	int findFriends( vector< int > s ) 
	{
		int numFriends = 0;
		int numStandingPeople = 0;
		for (int i = 0; i < s.size(); ++i)
		{
			int friendsNeeded = i > numStandingPeople;
			if (friendsNeeded > 0)
			{
				numFriends += friendsNeeded;
				numStandingPeople += friendsNeeded;
			}
			numStandingPeople += s[i];
		}
		return numFriends;
	}
};

int main()
{
	int T = 0;
	cin >> T;

	for (int i = 0; i < T; ++i)
	{
		int num = 0;
		cin >> num;

		string str;
		cin >> str;

		vector< int > s( str.length() );
		for (int j = 0; j < s.size(); ++j)
		{
			s[j] = str[j] - '0';
		}

		StandingOvation so;
		cout << "Case #" << i + 1 << ": " << so.findFriends( s ) << endl;
	}

	return 0;
}
