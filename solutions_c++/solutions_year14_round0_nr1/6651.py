#include <iostream>
#include <vector>
#include <string>
#include <string.h>
#include <stdio.h>
#include <sstream>
#include <algorithm>
#include <stdlib.h>

using namespace std;
int num_tests;
string guess1;
string guess2;
std::vector<string> row1, row2, row3, row4;
std::vector<string> row5, row6, row7, row8;

void cleanupVecs()
{
	row1.clear(); row2.clear(); row3.clear(); row4.clear();
	row5.clear(); row6.clear(); row7.clear(); row8.clear();
}

int findMatch(vector<string> &v1, vector<string> &v2)
{
	vector<string> v3;
	sort(v1.begin(), v1.end());
	sort(v2.begin(), v2.end());
	set_intersection(v1.begin(),v1.end(),v2.begin(),v2.end(),back_inserter(v3));
	//No possible matches, cheater
	if(v3.size() == 0) return -1;
	//Multiple matches, magician messed up
	else if(v3.size() > 1) return -2;
	else return atoi((*v3.begin()).c_str());
}

int lookMatch(){
	if(guess1=="1" && guess2=="1")
		return findMatch(row1,row5);
	if(guess1=="1" && guess2=="2")
		return findMatch(row1,row6);
	if(guess1=="1" && guess2=="3")
		return findMatch(row1,row7);
	if(guess1=="1" && guess2=="4")
		return findMatch(row1,row8);
	if(guess1=="2" && guess2=="1")
		return findMatch(row2,row5);
	if(guess1=="2" && guess2=="2")
		return findMatch(row2,row6);
	if(guess1=="2" && guess2=="3")
		return findMatch(row2,row7);
	if(guess1=="2" && guess2=="4")
		return findMatch(row2,row8);
	if(guess1=="3" && guess2=="1")
		return findMatch(row3,row5);
	if(guess1=="3" && guess2=="2")
		return findMatch(row3,row6);
	if(guess1=="3" && guess2=="3")
		return findMatch(row3,row7);
	if(guess1=="3" && guess2=="4")
		return findMatch(row3,row8);
	if(guess1=="4" && guess2=="1")
		return findMatch(row4,row5);
	if(guess1=="4" && guess2=="2")
		return findMatch(row4,row6);
	if(guess1=="4" && guess2=="3")	
		return findMatch(row4,row7);
	if(guess1=="4" && guess2=="4")
		return findMatch(row4,row8);
}

string input = "";
int t_num=1;
int main(){
	string num;
	getline(cin, num);
	stringstream ss(num);
	ss>>num_tests;
	while(num_tests>0){
		getline(cin,guess1);
		string tok;
		cout << "Case #" << t_num << ": ";
		t_num++;
		getline(cin,input);
		istringstream s1(input);
		while(getline(s1,tok,' '))
			row1.push_back(tok);
		input="";
		getline(cin,input);
		istringstream s2(input);
		while(getline(s2,tok,' '))
			row2.push_back(tok);
		input="";
		getline(cin,input);
		istringstream s3(input);
		while(getline(s3,tok,' '))
			row3.push_back(tok);
		input="";
		getline(cin,input);
		istringstream s4(input);
		while(getline(s4,tok,' '))
			row4.push_back(tok);
		input="";

		getline(cin,guess2);

		getline(cin,input);
		istringstream s5(input);
		while(getline(s5,tok,' '))
			row5.push_back(tok);
		input="";
		getline(cin,input);
		istringstream s6(input);
		while(getline(s6,tok,' '))
			row6.push_back(tok);
		input="";
		getline(cin,input);
		istringstream s7(input);
		while(getline(s7,tok,' '))
			row7.push_back(tok);
		input="";
		getline(cin,input);
		istringstream s8(input);
		while(getline(s8,tok,' '))
			row8.push_back(tok);
		input="";
		int m = lookMatch();
		if (m==-1) {
			cout << "Volunteer cheated!" << endl;
		} else if (m==-2) {
			cout << "Bad magician!" << endl;
		} else {
			cout << m << endl;
		}

		num_tests--;
		cleanupVecs();
	}
}
