#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>

using namespace std;

string problem(string s){
	map<char,int> lettercount;
	int numbercount[10];
	
	for(char c = 'A'; c <= 'Z'; c++)
		lettercount[c] = 0;
	for(int i = 0; i < 10; i++)
		numbercount[i] = 0;
	
	for(char c : s)
		lettercount[c]++;
	
	numbercount[0] = lettercount['Z'];
		lettercount['E'] -= lettercount['Z'];
		lettercount['R'] -= lettercount['Z'];
		lettercount['O'] -= lettercount['Z'];
		lettercount['Z'] = 0;
	numbercount[2] = lettercount['W'];
		lettercount['T'] -= lettercount['W'];
		lettercount['O'] -= lettercount['W'];
		lettercount['W'] = 0;
	numbercount[4] = lettercount['U'];
		lettercount['F'] -= lettercount['U'];
		lettercount['O'] -= lettercount['U'];
		lettercount['R'] -= lettercount['U'];
		lettercount['U'] = 0;
	numbercount[6] = lettercount['X'];
		lettercount['S'] -= lettercount['X'];
		lettercount['I'] -= lettercount['X'];
		lettercount['X'] = 0;
	numbercount[8] = lettercount['G'];
		lettercount['E'] -= lettercount['G'];
		lettercount['I'] -= lettercount['G'];
		lettercount['H'] -= lettercount['G'];
		lettercount['T'] -= lettercount['G'];
		lettercount['G'] = 0;
	numbercount[5] = lettercount['F'];
		lettercount['I'] -= lettercount['F'];
		lettercount['V'] -= lettercount['F'];
		lettercount['E'] -= lettercount['F'];
		lettercount['F'] = 0;
	numbercount[1] = lettercount['O'];
		lettercount['N'] -= lettercount['O'];
		lettercount['E'] -= lettercount['O'];
		lettercount['O'] = 0;
	numbercount[3] = lettercount['R'];
		lettercount['T'] -= lettercount['R'];
		lettercount['H'] -= lettercount['R'];
		lettercount['E'] -= 2 * lettercount['R'];
		lettercount['R'] = 0;
	numbercount[7] = lettercount['S'];
		lettercount['E'] -= 2 * lettercount['S'];
		lettercount['V'] -= lettercount['S'];
		lettercount['N'] -= lettercount['S'];
		lettercount['S'] = 0;
	numbercount[9] = lettercount['I'];
		lettercount['N'] -= 2 * lettercount['I'];
		lettercount['E'] -= lettercount['I'];
		lettercount['I'] = 0;
	
	string anss = "";
	for(int i = 0; i < 10; i++)
		for(int j = 0; j < numbercount[i]; j++)
			anss += to_string(i);
	
	return anss;
}

int main(){
	freopen("A-large.in", "r", stdin); freopen("A-large.out", "w", stdout);
	
	int n;
	cin >> n;
	
	string s;
	for(int i = 1; i <= n; i++){
		cin >> s;
		cout << "Case #" << i << ": " << problem(s) << endl;
	}
}
