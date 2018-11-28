#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <numeric>
using namespace std;

int remove_largest(vector<int> &members)
{
	auto i = max_element(members.begin(), members.end());
	if (*i == 0)
		return -1;
	int index = i - members.begin();
	members[index]--;
	return index;
}

bool has_majority(vector<int> &members)
{
	int total = accumulate(members.begin(), members.end(), 0);
	auto largest = max_element(members.begin(), members.end());
	int l = *largest;
	return l > total / 2;
}

string evacuate(vector<int> &members)
{
	string result = "";
	while (true)
	{
		int index = remove_largest(members);
		if (index == -1)
			break;
		result += ('A' + index);

		index = remove_largest(members);
		if (index != -1)
		{
			if (has_majority(members))
			{
				members[index]++;
			}
			else
			{
				result += ('A' + index);
			}
		}
		result += " ";
	}
	return result;
}

int main()
{
	int tests;
	cin >> tests;
	for(int test = 0; test < tests; ++test)
	{
		int parties;
		cin >> parties;
		vector<int> members;
		for(int j = 0; j < parties; ++j)
		{
			int party_members;
			cin >> party_members;
			members.push_back(party_members);
		}

		string plan = evacuate(members);
		cout << "Case #" << test+1 << ": " << plan << endl;
	}
}
