#include <iostream>
#include <string>
#include <vector>
#include <deque>
#include <set>
#include <map>
#include <iterator>
#include <algorithm>
#include <list>
#include<fstream>
using namespace std;
#define SZ(X) (int)(X.size()) 

int main()
{
	ifstream myReadFile;
	myReadFile.open("A-small-attempt2.in");
	int t ;
	myReadFile >> t ;
	vector<int> ans ;
	for(int k=0; k<t; k++)
	{
		int l;
		vector<vector<int>> cards(4,vector<int>(4)) ;
		vector<int> l1,l2,l3 ;

		myReadFile >> l ;
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)	
			{
				myReadFile >> cards[i][j] ;
				if(l-1 == i) l1.push_back(cards[i][j]) ;
			}

		myReadFile >> l ;
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
			{
				myReadFile >> cards[i][j] ;
				if(l-1 == i) l2.push_back(cards[i][j]) ;
			}

		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				if(l1[i] == l2[j])
					l3.push_back(l1[i]) ;

		if(SZ(l3) == 1)
			ans.push_back(l3[0]) ;
		else if(SZ(l3) > 1)
			ans.push_back(-1) ;
		else
			ans.push_back(0) ;
	}
	myReadFile.close();

	ofstream myfile;
	myfile.open ("out.txt");
	for(int i=0; i<SZ(ans); i++)
	{
		myfile << "Case #" << i+1 << ": " ;
		if(ans[i] == 0)
			myfile << "Volunteer cheated!\n" ;
		else if(ans[i] == -1)
			myfile << "Bad magician!\n" ;
		else
			myfile << ans[i] << endl ;
	} 
	myfile.close();
	return 0;
}