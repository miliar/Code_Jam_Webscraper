#include <iostream>
#include <cstring>
using namespace std;
int main(){
	int T;
	int l;
	int num[10];
	char freq[26];
	
	char str[2001];
	cin >> T;
	for(int t = 1;t <= T;t ++){
		for(int i = 0;i < 10;i ++){
			num[i] = 0;
		}
		for(int i = 0;i < 26;i ++){
			freq[i] = 0;
		}
		cin >> str;
		l = strlen(str);
		for(int i = 0;i < l;i ++){
			freq[str[i] - 65] ++;
		}
		
		while(freq['S' - 65] && freq['I' - 65] && freq['X' - 65]){
			num[6]++;
			freq['S' - 65] --;
			freq['I' - 65] --;
			freq['X' - 65] --;
		}
		
		while(freq['E' - 65] && freq['I' - 65] && freq['G' - 65] && freq['H' - 65] && freq['T' - 65]){
			num[8]++;
			freq['E' - 65] --;
			freq['I' - 65] --;
			freq['G' - 65] --;
			freq['H' - 65] --;
			freq['T' - 65] --;
		}
		
		while(freq['Z' - 65] && freq['E' - 65] && freq['R' - 65] && freq['O' - 65]){
			num[0]++;
			freq['Z' - 65] --;
			freq['E' - 65] --;
			freq['R' - 65] --;
			freq['O' - 65] --;
		}
		
		while(freq['T' - 65] && freq['W' - 65] && freq['O' - 65]){
			num[2]++;
			freq['T' - 65] --;
			freq['W' - 65] --;
			freq['O' - 65] --;
		}
		
		while(freq['T' - 65] && freq['H' - 65] && freq['R' - 65] && (freq['E' - 65] > 1)){
			num[3]++;
			freq['T' - 65] --;
			freq['H' - 65] --;
			freq['R' - 65] --;
			freq['E' - 65] -= 2;
		}
		
		while(freq['S' - 65] && (freq['E' - 65] > 1) && freq['V' - 65] && freq['N' - 65]){
			num[7]++;
			freq['S' - 65] --;
			freq['E' - 65] -= 2;
			freq['V' - 65] --;
			freq['N' - 65] --;
		}
		
		while(freq['F' - 65] && freq['O' - 65] && freq['U' - 65] && freq['R' - 65]){
			num[4]++;
			freq['F' - 65] --;
			freq['O' - 65] --;
			freq['U' - 65] --;
			freq['R' - 65] --;
		}
		
		while(freq['F' - 65] && freq['I' - 65] && freq['V' - 65] && freq['E' - 65]){
			num[5]++;
			freq['F' - 65] --;
			freq['I' - 65] --;
			freq['V' - 65] --;
			freq['E' - 65] --;
		}
		
		while((freq['N' - 65] > 1) && freq['I' - 65] && freq['E' - 65]){
			num[9]++;
			freq['N' - 65] -= 2;
			freq['I' - 65] --;
			freq['E' - 65] --;
		}
		
		
		while(freq['O' - 65] && freq['N' - 65] && freq['E' - 65]){
			num[1]++;
			freq['O' - 65] --;
			freq['N' - 65] --;
			freq['E' - 65] --;
		}
		
		
		cout << "Case #" << t << ": ";
		for(int i = 0;i < 10;i ++){
			for(int j = 0;j < num[i];j ++){
				cout << i;
			}
		}
		cout << endl;
	}
	return 0;
}
