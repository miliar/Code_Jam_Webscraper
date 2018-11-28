#include <iostream>
#include <set>

using namespace std;

int 
main(int argc, char *argv[])
{
	unsigned nrTCs = 0;
	cin >> nrTCs;

	for(unsigned i = 0; i < nrTCs; i++)
	{
		unsigned choice1 = 0, choice2 = 0;
		set <unsigned> order1;
		set <unsigned> order2;

		cin >> choice1;
		for(unsigned j = 0; j < 4; j++)
		{
			unsigned s1, s2, s3, s4;
			cin >> s1 >> s2 >> s3 >> s4;

			if (j + 1 == choice1)
			{
				order1.insert(s1);
				order1.insert(s2);
				order1.insert(s3);
				order1.insert(s4);
			}
		}

		cin >> choice2;
		for(unsigned j = 0; j < 4; j++)
		{
			unsigned s1, s2, s3, s4;
			cin >> s1 >> s2 >> s3 >> s4;

			if (j + 1 == choice2)
			{
				order2.insert(s1);
				order2.insert(s2);
				order2.insert(s3);
				order2.insert(s4);
			}
		}

		// Analysoi
		unsigned lastHit = 0, nrHits = 0;
		set <unsigned>::iterator It;
		for(It = order1.begin(); It != order1.end(); It++)
		{
			if (order2.find(*It) != order2.end())
			{
				nrHits++;
				lastHit = *It;
			}
		}

		cout << "Case #" << (i + 1) << ": ";
		if (nrHits == 0)
		{
			cout << "Volunteer cheated!\n";
		} else if (nrHits == 1)		
		{
			cout << lastHit << "\n";
		} else
		{
			cout << "Bad magician!\n";
		}
	}

	return 0;
}