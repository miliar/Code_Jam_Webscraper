#include <bits/stdc++.h>
using namespace std;

const string d[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

int cnt[1000];
int cnt_d[100];

void remove(int digit){
	for (int i=0; i<(int)d[digit].length(); i++)
		cnt[(int)d[digit][i]]-= cnt_d[digit];
}

void main2(){
	string s; cin >> s;
	for (int i=0; i<(int)s.size(); i++)
		cnt[(int)s[i]]++;
	cnt_d[0] = cnt['Z'];
	remove(0);
	cnt_d[6] = cnt['X'];
	remove(6);
	cnt_d[7] = cnt['S'];
	remove(7);
	cnt_d[8] = cnt['G'];
	remove(8);
	cnt_d[4] = cnt['U'];
	remove(4);
	cnt_d[5] = cnt['V'];
	remove(5);
	cnt_d[2] = cnt['W'];
	remove(2);
	cnt_d[1] = cnt['O'];
	remove(1);
	cnt_d[3] = cnt['T'];
	remove(3);
	cnt_d[9] = cnt['I'];
	remove(9);
	for (int i=0; i<10; i++)
		for (int j=0; j<cnt_d[i]; j++)
			cout << i;
	cout << endl;
}

int main(){
	int t; cin >> t;
	for (int o=1; o<=t; o++){
		cout << "Case #" << o << ": ";
		main2();
	}
	return 0;
}
