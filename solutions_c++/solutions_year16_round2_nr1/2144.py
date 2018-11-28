#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <stdlib.h>
#include <algorithm>

using namespace std;

int main(){
    int t;
	cin >> t;
	for(int i = 1; i <= t; i++){
		string s;
		int a[30], n = 1, num[700], k = 0;
		for(int j = 0; j < 30; j++)
			a[j] = 0;
		for(int j = 0; j < 700; j++)
			num[j] = 0;
		cin >> s;
		cout << "Case #" << i << ": ";
		for(int j = 0; j < s.size(); j++)
			a[s[j] - 'A']++;
		while(n > 0){
			n = 0;
			if(a['Z'-'A'] > 0){
				num[k++] = 0;
				a['Z'-'A']--;
				a['E'-'A']--;
				a['R'-'A']--;
				a['O'-'A']--;
			}
			else if(a['X'-'A'] > 0){
				num[k++] = 6;
				a['S'-'A']--;
				a['I'-'A']--;
				a['X'-'A']--;
			}
			else if(a['S'-'A'] > 0){
				num[k++] = 7;
				a['S'-'A']--;
				a['E'-'A']-= 2;
				a['V'-'A']--;
				a['N'-'A']--;	
			}
			else if(a['V'-'A'] > 0){
				num[k++] = 5;
				a['F'-'A']--;
				a['E'-'A']--;
				a['I'-'A']--;
				a['V'-'A']--;
			}
			else if(a['F'-'A'] > 0){
				num[k++] = 4;
				a['F'-'A']--;
				a['U'-'A']--;
				a['R'-'A']--;
				a['O'-'A']--;
			}
			else if(a['R'-'A'] > 0){
				num[k++] = 3;
				a['H'-'A']--;
				a['E'-'A']-= 2;
				a['R'-'A']--;
				a['T'-'A']--;
			}
			else if(a['H'-'A'] > 0){
				num[k++] = 8;
				a['H'-'A']--;
				a['E'-'A']--;
				a['G'-'A']--;
				a['I'-'A']--;
				a['T'-'A']--;
			}
			else if(a['T'-'A'] > 0){
				num[k++] = 2;
				a['O'-'A']--;
				a['W'-'A']--;
				a['T'-'A']--;
			}
			else if(a['O'-'A'] > 0){
				num[k++] = 1;
				a['E'-'A']--;
				a['N'-'A']--;
				a['O'-'A']--;
			}
			else {
				num[k++] = 9;
				a['N'-'A']--;
				a['E'-'A']--;
				a['I'-'A']--;
				a['N'-'A']--;
			}
			for(int j = 0; j < 26; j++)
				if(a[j] > 0)
					n++;
		}
		sort(num, num + k);
		for(int j = 0; j < k; j++)
			cout << num[j];
		cout << endl;
	}
	return 0;
}
