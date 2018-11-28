#include <cstdio>
#include <algorithm>
#include <set>
#include <vector>
using namespace std;

class Solution
{
	int m_testCase;
	int m_firstAnswer, m_secondAnswer;
	set<int> m_firstArrangement[4], m_secondArrangement[4];
public:
	Solution(int tc) : m_testCase(tc)
	{}
	void readInput()
	{
		scanf("%d", &m_firstAnswer);
		for (int i = 0; i < 4; ++i)
		{
			int val;
			for (int j = 0; j < 4; ++j)
			{
				scanf("%d", &val);
				m_firstArrangement[i].insert(val);
			}
		}

		scanf("%d", &m_secondAnswer);
		for (int i = 0; i < 4; ++i)
		{
			int val;
			for (int j = 0; j < 4; ++j)
			{
				scanf("%d", &val);
				m_secondArrangement[i].insert(val);
			}
		}
		--m_firstAnswer;
		--m_secondAnswer;
	}

	void solve()
	{
		vector<int> intersection(4, 0);
		std::set_intersection(
			m_firstArrangement[m_firstAnswer].begin(), 
			m_firstArrangement[m_firstAnswer].end(),
			m_secondArrangement[m_secondAnswer].begin(), 
			m_secondArrangement[m_secondAnswer].end(),
			intersection.begin());

		if (intersection[0] != 0 && intersection[1] == 0)
			printf("Case #%d: %d\n", m_testCase, intersection[0]);
		else if (intersection[1] != 0)
			printf("Case #%d: Bad magician!\n", m_testCase);
		else
			printf("Case #%d: Volunteer cheated!\n", m_testCase);
	}
};

int main()
{
	int testCases;
	scanf("%d", &testCases);
	for (int testCase = 1; testCase <= testCases; ++testCase)
	{
		Solution s(testCase);
		s.readInput();
		s.solve();
	}
	return 0;
}