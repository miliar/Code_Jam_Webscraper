// author : JongSeop Park, Koreatech
// contact: kugipark@gmail.com

#include <iostream>

class StandingOvation
{
protected:
	int maxShyness;
	char* nAudience;

public:
	StandingOvation() :
		nAudience(NULL)
	{
		onNewInput();
	}
	~StandingOvation()
	{
		if (nAudience)
		{
			delete[] nAudience;
		}
	}

public:
	int Solve()
	{
		int nAdditionalFriends = 0;
		int nStoodAudiences = (nAudience[0] - '0');
		for (int shylevel = 1; shylevel < (maxShyness + 1); shylevel++)
		{
			int nLackOfAudiences = shylevel - nStoodAudiences - nAdditionalFriends;
			if (nLackOfAudiences > 0)
			{
				nAdditionalFriends += nLackOfAudiences;
			}
			
			nStoodAudiences += (nAudience[shylevel] - '0');
		}

		return nAdditionalFriends;
	}

protected:
	void onNewInput()
	{
		std::cin >> maxShyness;

		nAudience = new char[maxShyness + 2];
		std::cin >> nAudience;
	}
};

int main(void)
{
	int nTestCases = 0;
	std::cin >> nTestCases;

	for (int i = 1; i <= nTestCases; i++)
	{
		StandingOvation standingOvation;
		int result = standingOvation.Solve();
		std::cout << "Case #" << i << ": " << result << std::endl;
	}

	return 0;

}