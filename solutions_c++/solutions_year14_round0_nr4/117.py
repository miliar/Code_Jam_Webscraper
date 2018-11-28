#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
#include <vector>
#include <algorithm>

using namespace std;


vector<double> my;
vector<double> his;
vector<double> myBack;
vector<double> hisBack;


ifstream fin("large.in");

int main(){
	int nt;
	fin >> nt;
	for(int t=0;t<nt;t++){
		my.clear();
		his.clear();
		int n;
		fin >> n;
		for(int i=0;i<n;i++){
			double tmp;
			fin >> tmp;
			my.push_back(tmp);
		}
		for(int i=0;i<n;i++){
			double tmp;
			fin >> tmp;
			his.push_back(tmp);
		}
		
		std::sort(his.begin(),his.end());
		std::sort(my.begin(),my.end());

		hisBack.assign(his.begin(),his.end());
		myBack.assign(my.begin(),my.end());

		//Deceitful War
		int deceitfulScore = 0;
		for(int i=0;i<n;i++){
			if(my.front() < his.front() || my.back() < his.back()){
				my.erase(my.begin());
				his.erase(his.end()-1);
			}
			else{
				my.erase(my.begin());
				his.erase(his.begin());
				deceitfulScore++;
			}
		}

		his.assign(hisBack.begin(),hisBack.end());
		my.assign(myBack.begin(),myBack.end());

		//War
		int regularScore = 0;
		for(int i=0;i<n;i++){
			if(my.back() > his.back()){
				regularScore++;
				my.erase(my.end()-1);
				his.erase(his.begin());
			}
			else{
				my.erase(my.end()-1);
				his.erase(his.end()-1);
			}
		}


		cout << "Case #" << t+1 << ": " <<  deceitfulScore << ' ' << regularScore << endl;
	}
	return 0;
}