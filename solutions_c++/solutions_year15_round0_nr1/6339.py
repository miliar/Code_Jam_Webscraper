#include <iostream>
#include <vector>
using namespace std;

int main()
{
	int shyMax;
	int ncases;
	int people;
	char dig;
	int total = 0;
	int invite = 0;
	
	cin >> ncases;
	
	for (int casenum = 1; casenum <= ncases; casenum++)
	{
		cin >> shyMax;
		for (int level = 0; level <= shyMax; level++)
		{
			cin >> dig;
			people = dig - '0';
			
	//cout << level << " " << people << " " << total << endl;
	
			if (people > 0 && level > total)
			{
			//cout << "add " << level-total << " people" << endl;
				invite += (level - total);
				total += (level - total);
			}
			total += people;
		}
		
		cout << "Case #" << casenum << ": " << invite << endl;
		
		total = 0;
		invite = 0;
	}
}

