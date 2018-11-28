#include <iostream>
#include <string>
#include <bitset>
#include <math.h>
#include <set>
#include <algorithm>
using namespace std;

int main()
{
	int T;
	int index = 1;
	cin >> T;
	while(T--){
		int num[27] = {0};
		int res[11] = {0};
		string str;
		cin >> str;
		int len = strlen(str.c_str());
		for (int i=0;i < len;i++){
			num[str[i]-'A'] ++;
		}
		while (num['Z'-'A'] > 0){
			num['Z'-'A']--;
			num['E'-'A']--;
			num['R'-'A']--;
			num['O'-'A']--;
			res[0]++;
		}
		while (num['G'-'A'] > 0){
			num['E'-'A']--;
			num['I'-'A']--;
			num['G'-'A']--;
			num['H'-'A']--;
			num['T'-'A']--;
			res[8]++;
		}
		while (num['X'-'A'] > 0){
			num['X'-'A']--;
			num['I'-'A']--;
			num['S'-'A']--;
			res[6]++;
		}
		while (num['H'-'A'] > 0){
			num['T'-'A']--;
			num['H'-'A']--;
			num['R'-'A']--;
			num['E'-'A']--;
			num['E'-'A']--;
			res[3]++;
		}
		while (num['S'-'A'] > 0){
			num['S'-'A']--;
			num['E'-'A']--;
			num['V'-'A']--;
			num['E'-'A']--;
			num['N'-'A']--;
			res[7]++;
		}
		while (num['V'-'A'] > 0){
			num['F'-'A']--;
			num['I'-'A']--;
			num['V'-'A']--;
			num['E'-'A']--;
			res[5]++;
		}
		while (num['W'-'A'] > 0){
			num['W'-'A']--;
			num['T'-'A']--;
			num['O'-'A']--;
			res[2]++;
		}
		while (num['R'-'A'] > 0){
			num['F'-'A']--;
			num['U'-'A']--;
			num['O'-'A']--;
			num['R'-'A']--;
			res[4]++;
		}
		while (num['O'-'A'] > 0){
			num['N'-'A']--;
			num['E'-'A']--;
			num['O'-'A']--;
			res[1]++;
		}
		while (num['E'-'A'] > 0){
			num['E'-'A']--;
			num['I'-'A']--;
			num['N'-'A']--;
			num['N'-'A']--;
			res[9]++;
		}
		cout << "Case #" << index++ << ": ";
		for (int i=0;i<10;i++){
			for (int j=0;j<res[i];j++){
				cout << i;
			}
		}
		cout << endl;
	}
	return 0;
}