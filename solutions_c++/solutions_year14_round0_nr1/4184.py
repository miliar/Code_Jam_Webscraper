//============================================================================
// Name        : Magic.cpp
// Author      : Moustafa Mohamed Ali
// Version     :
// Copyright   : 2014
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <bits/stdc++.h>
#include <fstream>
using namespace std;

int main() {
	freopen("A-small-attempt5.in","r",stdin);
	freopen("output.in","w",stdout);
	int nCases , q1Answer , q2Answer , c = 0 , choosen , Ncase = 1 ;
	vector <vector <int> > table (4);
	vector <vector <int> > second (4);
	cin>>nCases;
	while (nCases){
		cin>>q1Answer;
		for (int i = 0 ; i < 4 ; ++i )
			for (int j = 0 ; j < 4 ; ++j ){
				int temp ;
				cin>>temp;
				table[i].push_back(temp);
			}

		cin>>q2Answer;
		for (int i = 0 ; i < 4 ; ++i )
			for (int j = 0 ; j < 4 ; ++j ){
				int temp ;
				cin>>temp;
				second[i].push_back(temp);
			}

		for (int i = 0 ; i < 4 ; ++i ){
			for (int j = 0 ; j < 4 ; ++j ){
				if (table[q1Answer-1][i] == second[q2Answer-1][j] ){
					c++;
					choosen = table[q1Answer-1][i] ;
				}
			}
		}
		if (c == 0 )
			cout<<"Case #"<<Ncase<<": Volunteer cheated!"<<endl;
		else if (c > 1 )
			cout<<"Case #"<<Ncase<<": Bad magician!"<<endl;
		else if (c == 1 )
			cout<<"Case #"<<Ncase<<": "<<choosen<<endl;

		for (int i =0  ; i < 4 ; ++i ){
			table[i].clear();
			second[i].clear();
		}
		c = 0 ;
		Ncase++;
		nCases--;

	}
	return 0;
}
