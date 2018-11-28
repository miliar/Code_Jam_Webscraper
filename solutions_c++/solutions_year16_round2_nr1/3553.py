#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int cnt[30];
vector<int> ans;
void do_zero(){
	string x = "ZERO";
	while( cnt['Z' - 'A']){
		ans.push_back(0);
		for(int j = 0; j < x.size(); j++)
			cnt[ x[j] - 'A']--;
	}
}

void do_two(){
	string x = "TWO";
	while( cnt['W' - 'A']){
		ans.push_back(2);
		for(int j = 0; j < x.size(); j++)
			cnt[ x[j] - 'A']--;
	}
}

void do_six(){
	string x = "SIX";
	while( cnt['X' - 'A']){
		ans.push_back(6);
		for(int j = 0; j < x.size(); j++)
			cnt[ x[j] - 'A']--;
	}
}

void do_four(){
	string x = "FOUR";
	while( cnt['U' - 'A']){
		ans.push_back(4);
		for(int j = 0; j < x.size(); j++)
			cnt[ x[j] - 'A']--;
	}
}

void do_three(){
	string x = "THREE";
	while( cnt['R' - 'A']){
		ans.push_back(3);
		for(int j = 0; j < x.size(); j++)
			cnt[ x[j] - 'A']--;
	}
}

void do_eight(){
	string x = "EIGHT";
	while( cnt['H' - 'A']){
		ans.push_back(8);
		for(int j = 0; j < x.size(); j++)
			cnt[ x[j] - 'A']--;
	}
}

void do_one(){
	string x = "ONE";
	while( cnt['O' - 'A']){
		ans.push_back(1);
		for(int j = 0; j < x.size(); j++)
			cnt[ x[j] - 'A']--;
	}
}

void do_seven(){
	string x = "SEVEN";
	while( cnt['S' - 'A']){
		ans.push_back(7);
		for(int j = 0; j < x.size(); j++)
			cnt[ x[j] - 'A']--;
	}
}

void do_five(){
	string x = "FIVE";
	while( cnt['V' - 'A']){
		ans.push_back(5);
		for(int j = 0; j < x.size(); j++)
			cnt[ x[j] - 'A']--;
	}
}

void do_nine(){
	string x = "NINE";
	while( cnt['N' - 'A']){
		ans.push_back(0);
		for(int j = 0; j < x.size(); j++)
			cnt[ x[j] - 'A']--;
	}
}

int main() {

	int T; cin >> T;

	for(int t = 1; t <= T; t++){
		string w; cin >> w;
		ans.clear();
		for(int i = 0; i < w.size(); i++)
			cnt[ w[i] - 'A']++;

		//ZERO
		do_zero();
		do_two();
		do_six();
		do_four();
		do_three();
		do_eight();
		do_one();
		do_seven();
		do_five();
		do_nine();

		sort( ans.begin(), ans.end());

		cout << "Case #" << t << ": ";

		for(int i = 0; i < ans.size(); i++)
			cout << ans[i];
		cout << endl;
	}
	return 0;
}
