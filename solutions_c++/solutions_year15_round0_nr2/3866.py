// Pankakes.cpp : Definiert den Einstiegspunkt für die Konsolenanwendung.
//

#include "stdafx.h"


#include <iostream>
#include <iomanip>
#include <algorithm>
#include <map>
#include <set>
#include <vector>

using namespace std;

int OptTime(map<int,int> Diners)
{
	map<int,int>::reverse_iterator MaxPlate(Diners.rbegin());
	int NoSplit = MaxPlate->first;
	int Split;
	if(NoSplit>1) {
		Split=MaxPlate->second;
		int NumCakes = MaxPlate->first;
		Diners.erase(Diners.rbegin()->first);

		int BestTime = NoSplit;
		for(int s1 = 2; s1 <=NumCakes/2; s1++) {
			int s2 = NumCakes-s1; 
			Diners[s1] += Split;
			Diners[s2] += Split;
			int SplitRes=OptTime(Diners);
			Diners[s1] -= Split;
			Diners[s2] -= Split;
			if (SplitRes<BestTime) BestTime = SplitRes;
		}
		Split+=BestTime;
	}
	else {Split=NoSplit;}
	return min(Split,NoSplit);
}


int _tmain(int argc, _TCHAR* argv[])
{

	int T;
	cin >> T;
	for(int NumCase=1; NumCase <=T; NumCase++) {
		int Res(0), NumDiners;
		map<int,int> Diners;
		cin >> NumDiners;
		for( int i=0; i < NumDiners; i++) { 
			int in;
			cin >> in;
			Diners[in] = Diners[in]+1;
		}

		map<int,int>::reverse_iterator MaxPlate(Diners.rbegin());
#if 0
		while(MaxPlate != Diners.rend() && MaxPlate->first/2 > MaxPlate->second) {
			//split
			Res++;
			int s1 = MaxPlate->first/2;
			int s2 = MaxPlate->first-s1; 
			Diners[s1] += 1;
			Diners[s2] += 1;
			if(MaxPlate->second > 1) (MaxPlate->second)--; 
			else Diners.erase(MaxPlate->first);
			MaxPlate = Diners.rbegin();
		}
		Res+=MaxPlate->first;
#else
		Res = OptTime(Diners);
#endif
		cout << "Case #" << NumCase << ": " << Res;
		cout << endl;
	}
	return 0;
}
