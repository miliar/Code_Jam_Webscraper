#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <string>

using namespace std;

int main(){
	int test;
	cin>>test;
	string p[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };

	for (int k = 1;k <= test;k++){
		int a[256] = {0};
		string s;
		cin >> s;
		int len = s.length();
		for(int i = 0;i < len;i++){
			int temp = s[i];
			a[temp]++;
		}
		int i = 0;
		int temp = 'Z';
		int cnt = 0;
		int ans[10] = {0};
		if(a[temp] != 0){
			cnt = a[temp];
			a[temp] -= cnt;
			ans[0] = cnt;
			temp = 'E';
			a[temp] -= cnt;
			temp = 'R';
			a[temp] -= cnt;
			temp = 'O';
			a[temp] -= cnt;
		}
		temp = 'X';
		 if(a[temp] != 0){
			cnt = a[temp];
			a[temp] -= cnt;
			ans[6] = cnt;
			temp = 'S';
			a[temp] -= cnt;
			temp = 'I';
			a[temp] -= cnt;
		}
		temp = 'G';
		 if(a[temp] != 0){
			cnt = a[temp];
			a[temp] -= cnt;
			ans[8] = cnt;
			temp = 'E';
			a[temp] -= cnt;
			temp = 'I';
			a[temp] -= cnt;
			temp = 'H';
			a[temp] -= cnt;
			temp = 'T';
			a[temp] -= cnt;
		}
		temp = 'W';
		 if(a[temp] != 0){
			cnt = a[temp];
			a[temp] -= cnt;
			ans[2] = cnt;
			temp = 'T';
			a[temp] -= cnt;
			temp = 'O';
			a[temp] -= cnt;
		}
		temp = 'H';
		 if(a[temp] != 0){
			cnt = a[temp];
			a[temp] -= cnt;
			ans[3] = cnt;
			temp = 'R';
			a[temp] -= cnt;
			temp = 'T';
			a[temp] -= cnt;
			temp = 'E';
			a[temp] -= cnt;
			temp = 'E';
			a[temp] -= cnt;
		}
		temp = 'U';
		 if(a[temp] != 0){
			cnt = a[temp];
			a[temp] -= cnt;
			ans[4] = cnt;
			temp = 'F';
			a[temp] -= cnt;
			temp = 'O';
			a[temp] -= cnt;
			temp = 'R';
			a[temp] -= cnt;
		}
		temp = 'F';
		 if(a[temp] != 0){
			cnt = a[temp];
			a[temp] -= cnt;
			ans[5] = cnt;
			temp = 'I';
			a[temp] -= cnt;
			temp = 'V';
			a[temp] -= cnt;
			temp = 'E';
			a[temp] -= cnt;
		}
		temp = 'I';
		 if(a[temp] != 0){
			cnt = a[temp];
			a[temp] -= cnt;
			ans[9] = cnt;
			temp = 'N';
			a[temp] -= cnt;
			temp = 'N';
			a[temp] -= cnt;
			temp = 'E';
			a[temp] -= cnt;
		}
		temp = 'V';
		 if(a[temp] != 0){
			cnt = a[temp];
			a[temp] -= cnt;
			ans[7] = cnt;
			temp = 'N';
			a[temp] -= cnt;
			temp = 'S';
			a[temp] -= cnt;
			temp = 'E';
			a[temp] -= cnt;
			temp = 'E';
			a[temp] -= cnt;
		}
		temp = 'O';
		 if(a[temp] != 0){
			cnt = a[temp];
			a[temp] -= cnt;
			ans[1] = cnt;
			temp = 'N';
			a[temp] -= cnt;
			temp = 'E';
			a[temp] -= cnt;
		}
		cout << "Case #"<<k<<": ";
		for (int i = 0;i < 10;i++){
			for(int j = 0;j < ans[i];j++){
				cout<<i;
			}
		}
		cout<<"\n";
		// cout <<'Case: '<<i<<
	}
}