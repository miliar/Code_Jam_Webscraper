//============================================================================
// Name        : Pancakes.cpp
// Author      : Yao Zhang
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <set>
using namespace std;

int caltime(multiset<int> pank){
	if(*pank.rbegin() <=3)
		return *pank.rbegin();
	else{
		int i = *pank.rbegin();
		int use9 = 10;

		if(i ==9){
			multiset<int> nPank(pank);
			nPank.erase(--nPank.end());
			nPank.insert(3);
			nPank.insert(3);
			nPank.insert(3);
			use9 = caltime(nPank) + 2;
			nPank.clear();
		}
		int x = i/2;
		int y = i/2 + i%2;
		pank.erase(--pank.end());
		pank.insert(x);
		pank.insert(y);
		int use = caltime(pank) + 1;
		use = use < use9 ?use:use9;
		return use < i?use:i;
	}
}
int main() {
	int total;
	ifstream infile("input.txt");
	ofstream SaveFile("output.txt");
	if (infile.is_open()){
		int people;
		multiset<int> pancake;
		int time;
		infile>>total;
		for(int i=0; i<total; i++){
			infile>>people;
			for(int i=0;i<people;i++){
				int j;
				infile>>j;
				pancake.insert(j);
			}
			time = caltime(pancake);
			cout<<"Case #"<<i+1<<": "<< time<<endl;
			SaveFile<<"Case #"<<i+1<<": "<< time<<endl;
			pancake.clear();
		}
		infile.close();
		SaveFile.close();
	}

	else{
			cout<<"Error,can't open...\n";
			exit(2);
	}
}
