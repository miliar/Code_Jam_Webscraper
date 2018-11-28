#include <iostream>
#include <fstream>
#include <limits>

#define S_MAX	1000

using namespace std;

int	char2digit(char ch)
{
	switch(ch)
	{
		case '0': return 0;
		case '1': return 1;
		case '2': return 2;
		case '3': return 3;
		case '4': return 4;
		case '5': return 5;
		case '6': return 6;
		case '7': return 7;
		case '8': return 8;
		case '9': return 9;
	}
	return -1;
}

int	handleTestCase(int sMax, int sArr[])
{
	int	tc = 0;	// tc -> totalClappers
	int	ra = 0;	// ra -> requiredAudience
	
	//~ cout << "\n\t sMax=" << sMax << "| ";
	//~ for(int i = 0; i <= sMax; ++i)
		//~ cout << "[" << sArr[i] << "] ";




	// Assumption: There will always be at least one person in the audience. 
	int	currentNeed = 0;
	for(int i = 0; i <= sMax; ++i)
	{
		if(sArr[i] != 0)
		{
			if(tc < i)
			{
				currentNeed = i - tc;
				ra += currentNeed;
				tc += currentNeed;
			}
			tc += sArr[i];
		}
	}
	
	
	return ra;
}

int	main()
{
	int		t;
	string		sArrStr;
	int		sArr[S_MAX+1];
	int		sMax;
	int		requiredAudience;

	ifstream	ifs;
	ofstream	ofs;




	ifs.open("A-large.in", ios::in);
	if(!ifs.is_open())
	{
		cout << "\n\tUnable to open IN file...";
		return 1;
	}
	ofs.open("A-small-attempt0.out", ios::out);
	if(!ofs.is_open())
	{
		cout << "\n\tUnable to open OUT file...";
		return 1;
	}




	ifs >> t;
	//~ cout << "\n\t t=" << t;
	for(int i = 0; i < t; ++i)
	{
		ifs >> sMax;
		ifs.ignore(std::numeric_limits<std::streamsize>::max(), ' ');	// Should be placed here...
		getline(ifs, sArrStr);
		for(int j = 0; j <= sMax; ++j)
			sArr[j] = char2digit(sArrStr[j]);

		requiredAudience = handleTestCase(sMax, sArr);

		ofs << "Case #" << i+1 << ": " << requiredAudience << endl;
	}

	return 0;
}
