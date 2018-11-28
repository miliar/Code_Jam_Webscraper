#include <iostream>
#include <string>
#include <vector>
#include <limits.h>
#include <cmath>

using namespace std;

struct Group {
	char c;
	int pos;
	int cnt;
};

void solveCase(int caseNum){

	int stringsNum;
	
	cin >> stringsNum;
	cin.ignore();

	vector< vector<Group> > chargroups;

	string buff;
	for(int i=0; i < stringsNum ; i++){
		buff.clear();
		getline(cin,buff);
		vector<Group> g;

		//cout << buff << endl;
		for(int j=0;j<buff.size();j++){

			Group group;
			group.c = buff[j];
			group.pos = j;
			group.cnt = 0;

			int p = j;
			for(; p< buff.size(); p++){
				if(buff[j] == buff[p]){
					group.cnt++;					
				}
				else{
					j = p -1;
					break;
				}
			}

			g.push_back(group);
			if(p == buff.size())
				break;
		}
		chargroups.push_back(g);
	}



	/*
	for(const auto & group : chargroups){
		for(const auto & g : group){
			cout << g.c << " " << g.pos << " " << g.cnt << " : ";
		}
		cout << endl;
	}*/


	int actions = 0;

	for(int groupid=0;groupid < chargroups[0].size();groupid++){
		Group g1 = chargroups[0][groupid];

		double avg = g1.cnt;
		char c= g1.c;



		for(int stringid = 1; stringid < chargroups.size(); stringid++){
			Group g2 = chargroups[stringid][groupid];
		


			avg += g2.cnt;

			if(g2.c != c || chargroups[0].size() != chargroups[stringid].size()) {
				cout << "Case #" << caseNum << ": Fegla Won" << endl;
				return;
			}
		}
		//cout <<"avga: " << avg << endl;
		avg /= chargroups.size();
		//cout <<"avgb: " << avg << endl;

		avg = round(avg);
		//cout <<"avgc: " << avg << endl;


		for(int stringid = 0; stringid < chargroups.size(); stringid++){
			Group g = chargroups[stringid][groupid];
			actions+=abs(g.cnt - avg);
		}

	}


	cout << "Case #" << caseNum << ": " << actions << endl;



}



int main(void){

	int numCases;
	cin >> numCases;

	for(int i=1; i<=numCases;i++){
		solveCase(i);
	}

}