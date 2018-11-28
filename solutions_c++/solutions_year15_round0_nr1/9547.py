//============================================================================
// Name        : StandingOvation.cpp
// Author      : David Sánchez
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
using namespace std;

inline int resolve(const int &maxsh, const char shylev[])
{
	int invited = 0;
	int clapping = 0;
	int bubble;
	clapping = shylev[0] - '0';
	for(int i = 1; i <= maxsh; i++)
	{
		bubble = shylev[i] - '0';
		if(i > clapping)
		{
			invited += i - clapping;
			clapping = i;
		}
		clapping += bubble;
	}
	return invited;
}

int main() {
	int testcases = 0;
	int maxshyness = 0;
	char cad[1002] = {0};

	cin >> testcases;
	for(int i = 1; i <= testcases; i++)
	{
		cin >> maxshyness >> cad;
		cout << "Case #"<< i << ": " << resolve(maxshyness, cad) << endl;
	}
	return 0;
}
