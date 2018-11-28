#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <list>
#include <algorithm>

#define FILE

using namespace std;

long long int getCount(long long int rad,long long int ink)
{
	long long int count=0;
	long long int blackRad = rad+1;
	long long int whiteRad = rad;
	long long int require=(blackRad*blackRad)-(whiteRad*whiteRad);
	
	while(require <= ink){
		++count;
		blackRad+=2;
		whiteRad+=2;
		require += (blackRad*blackRad)-(whiteRad*whiteRad);
	}
	
	return count;
}

int main()
{
	ofstream ofs("/Users/iseki/Downloads/ans.dat");
	int T;
#ifdef FILE
	ifstream ifs( "/Users/iseki/Downloads/A-small-attempt1.in" );
	ifs >> T;
#endif
#ifndef FILE
	cin >> T;
#endif
	long long int rad,ink,count;
	for (int caseNum=1; caseNum<=T; ++caseNum) {
#ifdef FILE
		ifs >> rad >> ink;
#endif
#ifndef FILE
		cin >> rad >> ink;
#endif

		count = getCount(rad,ink);
		
		cout << "Case #" << caseNum << ": " ;
		cout << count << endl;
		ofs << "Case #" << caseNum << ": " ;
		ofs << count << endl;
	}
	
	return 0;
}