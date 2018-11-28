#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <map>

using namespace std;

/*
int count(string s, char c) {
	count = 0;
	for(auto ch = s.begin(); ch < s.end(); ch++)
		if(ch == c) count++;
	return count;
}
*/
void solve(string s){
	map<char, int> counts;
	for(auto ch = s.begin(); ch != s.end(); ch++) {
		auto f = counts.find(*ch);
		if(f != counts.end())
			f->second++;
		else
			counts.insert(make_pair(*ch, 1));
	}


	//remove ZERO
	int count0 = 0;
	auto x0 = counts.find('Z');
	if(x0 != counts.end())
		count0 = x0->second;

	int count6 = 0;
	auto x6 = counts.find('X');
	if(x6 != counts.end())
		count6 = x6->second;

	int count2 = 0;
	auto x2 = counts.find('W');
	if(x2 != counts.end())
		count2 = x2->second;

	int count4 = 0;
	auto x4 = counts.find('U');
	if(x4 != counts.end())
		count4 = x4->second;

	int count8 = 0;
	auto x8 = counts.find('G');
	if(x8 != counts.end())
		count8 = x8->second;

	int count1 = 0;
	auto x1 = counts.find('O');
	if(x1 != counts.end())
		count1 = x1->second - count0 - count2 - count4;

	int count3 = 0;
	auto x3 = counts.find('T');
	if(x3 != counts.end())
		count3 = x3->second - count8 - count2;

	int count5 = 0;
	auto x5 = counts.find('F');
	if(x5 != counts.end())
		count5 = x5->second - count4;

	int count7 = 0;
	auto x7 = counts.find('V');
	if(x7 != counts.end())
		count7 = x7->second - count5;

	int count9 = 0;
	auto x9 = counts.find('I');
	if(x9 != counts.end())
		count9 = x9->second - count8 - count6 - count5;

	for(int i = 0; i < count0; i++)
		cout << "0";
	for(int i = 0; i < count1; i++)
		cout << "1";
	for(int i = 0; i < count2; i++)
		cout << "2";
	for(int i = 0; i < count3; i++)
		cout << "3";
	for(int i = 0; i < count4; i++)
		cout << "4";
	for(int i = 0; i < count5; i++)
		cout << "5";
	for(int i = 0; i < count6; i++)
		cout << "6";
	for(int i = 0; i < count7; i++)
		cout << "7";
	for(int i = 0; i < count8; i++)
		cout << "8";
	for(int i = 0; i < count9; i++)
		cout << "9";
}

int main() {
	int t;
	string s;

	cin >> t;

	for(int i = 0; i < t; i++){
		cin >> s;
		cout << "Case #" << (i + 1) << ": ";
		solve(s);
		cout << endl;
	}

	return EXIT_SUCCESS;
}
