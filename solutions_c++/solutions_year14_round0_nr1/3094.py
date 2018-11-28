// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream f;
	f.open("Asmall.in");
	ofstream of;
	of.open("out.txt");
	int nbr_of_testcases;
	f >> nbr_of_testcases;
	for (int i = 1; i<=nbr_of_testcases ; i++) {
		vector<int> first;
		vector<int> possible;
		int ans1;
		f >>ans1;
		int in;
		for(int j = 1; j!=5; j++) {

			for(int x = 1; x!=5;x++) {
				if(j == ans1) {
					f >> in;
					first.push_back(in);
				} else {
					f>> in;
				}
			}
		}
		int ans2;
		f >>ans2;
		for(int y=1;y!=5;y++) {
			for(int x = 1; x!=5;x++) {
				if(y == ans2) {
					f >> in;
					if(find(first.begin(),first.end(),in)!=first.end())  
						possible.push_back(in);
				} else {
					f>> in;
				}
			}
		}
		if(possible.size()==0){
			of << "Case #" << i << ": Volunteer cheated!" << endl;
		}else if(possible.size() == 1) {
			of << "Case #" << i << ": " << possible[0] << endl;
		} else {
			of << "Case #" << i << ": Bad magician!" << endl;
		}
	}
	


}

