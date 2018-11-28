#include <iostream>
#include <vector>
#include <string.h>
#include <stack>
#include <algorithm>

typedef struct
{
	int openKey;
	std::vector<int> keys;
} Chest;

std::vector<Chest> Chests;
std::stack <int> Result;

class Node
{
public:
	int keysInHand[200];
	int keyDependencies[200];
	int keysLeft[200];
	std::vector<int> chestsNotOpened; // mieti tätä

public:
	Node(Node &n)
		: chestsNotOpened(n.chestsNotOpened)
	{
		memcpy(keysInHand, n.keysInHand, sizeof(keysInHand));
		memcpy(keyDependencies, n.keyDependencies, sizeof(keyDependencies));
		memcpy(keysLeft, n.keysLeft, sizeof(keysLeft));
	}
	Node()
	{
		memset(keysInHand, 0, sizeof(keysInHand));
		memset(keyDependencies, 0, sizeof(keyDependencies));
		memset(keysLeft, 0, sizeof(keysLeft));
	}
};

bool openChests(Node &n)
{
	// Lopetusehto?
	if (n.chestsNotOpened.size() == 0)
	{
		return true;
	}

	for(unsigned i = 0; i < n.chestsNotOpened.size(); i++)
	{
		int chestID = n.chestsNotOpened[i];
		int openKeyID = Chests[chestID].openKey;

		if (n.keysInHand[openKeyID] > 0)
		{
			// Does this one release keys?
			int keyRelease = std::count(Chests[chestID].keys.begin(), Chests[chestID].keys.end(), openKeyID);

			if  (n.keyDependencies[openKeyID] && n.keysLeft[openKeyID] - 1 == n.keyDependencies[openKeyID] && keyRelease == 0)
			{
				continue;
			}

			Node n2(n);
			n2.chestsNotOpened.erase (n2.chestsNotOpened.begin() + i);
			n2.keyDependencies[openKeyID] -= keyRelease;
			n2.keysInHand[Chests[chestID].openKey]--;
			n2.keysLeft[Chests[chestID].openKey]--;
			for(unsigned j = 0; j < Chests[chestID].keys.size(); j++)
			{
				n2.keysInHand[Chests[chestID].keys[j]]++;
			}

			if (openChests(n2))
			{
				Result.push(chestID);
				return true;
			}
		}
	}
	
	return false;
}

int main(int argc, char *argv[])
{
	int nrTestCases;

	std::cin >> nrTestCases;

	for(int tc = 0; tc < nrTestCases; tc++)
	{
		Node startingNode;
		int nrKeys, nrChests;
		int keysAvailable[200];
		int keysNeeded[200];

		memset(keysAvailable, 0, sizeof(keysAvailable));
		memset(keysNeeded, 0, sizeof(keysNeeded));

		std::cin >> nrKeys >> nrChests;

		std::vector<int> startingKeys;
		for(int i = 0; i < nrKeys; i++)
		{
			int nr;
			std::cin >> nr;
			startingNode.keysInHand[nr]++;
			keysAvailable[nr]++;
			// startingKeys.push_back(nr);
		}

		Chests.clear();
		for(int i = 0; i < nrChests; i++)
		{
			Chest c;
			std::cin >> c.openKey;
			keysNeeded[c.openKey]++;
			int nr;
			std::cin >> nr;
			for(int j = 0; j < nr; j++)
			{
				int key;
				std::cin >> key;
				c.keys.push_back(key);
				keysAvailable[key]++;
			}
			Chests.push_back(c);
		}

		// Push numbers of all chests.
		for(unsigned i = 0; i < Chests.size(); i++)
		{
			startingNode.chestsNotOpened.push_back(i);
		}

		std::cout << "Case #" << (tc +1) << ":";

		// Test are there enough keys supplied?
		for(int i = 0; i < 200; i++)
		{
			if (keysAvailable[i] < keysNeeded[i])
			{
				std::cout << " IMPOSSIBLE";
				goto end;
			}
		}

		// Test are there key loops?
		for(unsigned i = 0; i < Chests.size(); i++)
		{
			int openKeyApperances = std::count(Chests[i].keys.begin(), Chests[i].keys.end(), Chests[i].openKey);
			startingNode.keyDependencies[Chests[i].openKey] += openKeyApperances;
		}

		for(int i = 0; i < 200; i++)
		{
			startingNode.keysLeft[i] = keysAvailable[i];
		}

		// Empty the result
		while(!Result.empty())
		{
			Result.pop();
		}

		// Calculate
		if (!openChests(startingNode))
		{
			std::cout << " IMPOSSIBLE";
		} else 
		{
			while(!Result.empty())
			{
				int r = Result.top();
				Result.pop();
				std::cout << " " << (r + 1);
			}
		}

		end:
		std::cout << "\n";
	}

	return 0;
}