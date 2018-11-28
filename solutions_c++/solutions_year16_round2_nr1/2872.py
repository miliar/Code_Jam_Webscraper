#include<cstdio>
#include<cmath>
#include<iostream>
#include<fstream>
#include<string>
#include<queue>
#include<vector>
#include<set>
#include<map>
#include<algorithm>
using namespace std;

#define STOP {cin.sync();cin.get();}
#define f0(i, n) for(int i=0; i<(int)(n);i++)
#define f1(i, n) for(int i=1; i<=(int)(n);i++)

ifstream fin("A-large.in");
ofstream fout("output.txt");

int T;
char S[2000];

void solve(int num){
	//cin >> S;
	fin >> S;

	map<char, int> judge;
	vector<int> ans;

	f0(i, 2000){
		char a = S[i];
		if (a == NULL)	break;
		else if (judge.find(a) == judge.end()){
			judge.insert(make_pair(a, 1));
		}
		else{
			judge[a]++;
		}
	}

	//0
	if (judge.find('Z') != judge.end()){
		f0(i, judge['Z'])	ans.push_back(0);
		judge['E'] -= judge['Z'];
		judge['R'] -= judge['Z'];
		judge['O'] -= judge['Z'];
		judge['Z'] = 0;
	}
	//2
	if (judge.find('W') != judge.end()){
		f0(i, judge['W'])	ans.push_back(2);
		judge['T'] -= judge['W'];
		judge['O'] -= judge['W'];
		judge['W'] = 0;
	}
	//4
	if (judge.find('U') != judge.end()){
		f0(i, judge['U'])	ans.push_back(4);
		judge['F'] -= judge['U'];
		judge['O'] -= judge['U'];
		judge['R'] -= judge['U'];
		judge['U'] = 0;
	}
	//6
	if (judge.find('X') != judge.end()){
		f0(i, judge['X'])	ans.push_back(6);
		judge['S'] -= judge['X'];
		judge['I'] -= judge['X'];
		judge['X'] = 0;
	}
	//1
	if (judge.find('O') != judge.end()){
		f0(i, judge['O'])	ans.push_back(1);
		judge['N'] -= judge['O'];
		judge['E'] -= judge['O'];
		judge['O'] = 0;
	}
	//3
	if (judge.find('R') != judge.end()){
		f0(i, judge['R'])	ans.push_back(3);
		judge['T'] -= judge['R'];
		judge['H'] -= judge['R'];
		judge['E'] -= judge['R'] * 2;
		judge['R'] = 0;
	}
	//5
	if (judge.find('F') != judge.end()){
		f0(i, judge['F'])	ans.push_back(5);
		judge['V'] -= judge['F'];
		judge['I'] -= judge['F'];
		judge['E'] -= judge['F'];
		judge['F'] = 0;
	}
	//7
	if (judge.find('V') != judge.end()){
		f0(i, judge['V'])	ans.push_back(7);
		judge['S'] -= judge['V'];
		judge['E'] -= judge['V'] * 2;
		judge['V'] -= judge['V'];
		judge['N'] = 0;
	}
	//8
	if (judge.find('G') != judge.end()){
		f0(i, judge['G'])	ans.push_back(8);
		judge['E'] -= judge['G'];
		judge['I'] -= judge['G'];
		judge['H'] -= judge['G'];
		judge['T'] -= judge['G'];
		judge['G'] = 0;
	}
	//9
	if (judge.find('E') != judge.end()){
		f0(i, judge['E'])	ans.push_back(9);
		judge['N'] -= judge['E'];
		judge['I'] -= judge['E'];
		judge['E'] = 0;
	}

	sort(ans.begin(), ans.end());

	//cout << "Case #" << num << ": ";
	//f0(i, ans.size())	cout << ans[i];
	//cout << endl;
	fout << "Case #" << num << ": ";
	f0(i, ans.size())	fout << ans[i];
	fout << endl;
}

int main(){
	//cin >> T;
	fin >> T;

	f1(num, T){
		solve(num);
	}

	//STOP;

	return 0;
}