#include <iostream>
#include <vector>
#include <queue>

using Party = std::pair<int, int>;

struct PartyCompare
{
	bool operator()(const Party& p1, const Party& p2) const
	{
		return p1.second < p2.second;
	}
};

using PartySet = std::priority_queue<Party, std::vector<Party>, PartyCompare>;

std::pair<int, int> EvacuateStep(PartySet& parties, int members)
{
	int majority1 = (members - 1) / 2;
	int majority2 = (members - 2) / 2;

	auto firstEntry = parties.top();
	parties.pop();

	auto firstParty = firstEntry.first;
	auto members1 = firstEntry.second;

	if (members == 1)
	{
		return {firstParty, -1};
	}

	if (members == 2 && parties.empty())
	{
		return {firstParty, firstParty};
	}

	if ((members1 >= 2) && ((members1 - 2) <= majority2))
	{
		if (parties.top().second <= majority2) // 
		{
			if (members1 > 2)
			{
				parties.emplace(firstParty, members1 - 2);
			}
			return {firstParty, firstParty};
		}
	}

	if ((members1 - 1) > majority2)
	{
		if (parties.empty() || ((parties.top().second - 1) <= majority1))
		{
			if (members1 > 1)
			{
				parties.emplace(firstParty, members1 - 1);
			}
			return {firstParty, -1};
		}
	}

	if (members == 3 && parties.size() == 2)
	{
		return {firstParty, -1};
	}

	auto secondEntry = parties.top();
	parties.pop();

	auto secondParty = secondEntry.first;
	auto members2 = secondEntry.second;

	if (members1 > 1)
	{
		parties.emplace(firstParty, members1 - 1);
	}

	if (members2 > 1)
	{
		parties.emplace(secondParty, members2 - 1);
	}	

	return {firstParty, secondParty};
}


int main()
{
	int T;
	std::cin >> T;
	for (int i = 1; i <= T; ++i)
	{
		PartySet pq;
		int N;
		int members = 0;
		std::cin >> N;
		for (int k = 0; k < N; ++k)
		{
			int num;
			std::cin >> num;
			pq.emplace(k, num);
			members += num;
		}
		std::cout << "Case #" << i << ": ";
		while (members)
		{
			auto sol = EvacuateStep(pq, members);
			if (sol.second == -1)
			{
				std::cout << (char)('A' + sol.first);
				--members;
			}
			else
			{
				std::cout << (char)('A' + sol.first) << (char)('A' + sol.second);
				members -= 2;
			}

			if (members > 0)
			{
				 std::cout << " ";
			}
		}
		std::cout << "\n";
	}
	return 0;
}