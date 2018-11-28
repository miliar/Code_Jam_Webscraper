#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
#include <map>
#include <sstream>

using namespace std;

int main()
{
//	ifstream in("A-small-attempt0.in");
//	ofstream out("A-small-attempt0.out");

	ifstream in("A-large.in");
	ofstream out("A-large.out");
	int iTasks;
	in >> iTasks;
	int baseDigit = '0';
	for( int iCount = 1; iCount <= iTasks; iCount++ )
	{
		int maxShy = 0;
		in >> maxShy;

		string sShys;
		in >> sShys;

		int alreadyStand = 0;
		int needToInvite = 0;
		
		for (int i = 0; i <= maxShy; i++)
		{
			int additionalInvite = 0;
			if (i > alreadyStand)
				additionalInvite = i - alreadyStand;
			
			needToInvite += additionalInvite;
			alreadyStand += additionalInvite + sShys[i] - baseDigit;
			
		}
		out << "Case #" << iCount << ": " << needToInvite << endl;
	}
	return 0;
}
