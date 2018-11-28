#include <iostream>
#include <queue>
#include <utility>
using namespace std;


struct Party
{
	char name;
	int numSenators;

	static bool compare(Party &p1, Party &p2)
	{
		if (p1.numSenators < p2.numSenators)
			return true;
		else if (p1.numSenators > p2.numSenators)
			return false;
		else
			return (p1.name > p2.name);
	}
};



Party parties[26];

int main()
{
	for (int i = 0; i < 26; i++)
		parties[i].name = 'A' + i;

	int numTestCases;
	scanf("%d", &numTestCases);
	for (int t = 0; t < numTestCases; t++)
	{
		int numParties;
		scanf("%d", &numParties);
		int totalPeople = 0;
		priority_queue<Party, std::vector<Party>, decltype(&Party::compare)> pq(&Party::compare);
		for (int i = 0; i < numParties; i++)
		{
			int p;
			scanf("%d", &p);
			totalPeople += p;
			parties[i].numSenators = p;
			pq.push(parties[i]);
		}

		cout << "Case #" << t+1 << ":";
		while (totalPeople > 0)
		{
			char c1;

			Party p = pq.top();
			pq.pop();
			p.numSenators--;
			if (p.numSenators != 0)
				pq.push(p);
			cout << " " << p.name;
			totalPeople--;


			if (totalPeople != 2)
			{
				Party p = pq.top();
				pq.pop();
				p.numSenators--;
				if (p.numSenators != 0)
					pq.push(p);
				cout << p.name;
				totalPeople--;
			}
		}	
		cout << endl;	
	}
}