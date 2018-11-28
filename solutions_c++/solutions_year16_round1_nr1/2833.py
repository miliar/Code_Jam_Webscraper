#include <bits/stdc++.h>

using namespace std;


int main(){
	ios::sync_with_stdio(false);
	int t;
	long long n;
	cin >> t;
	int caso = 1;
	string str;
	while(t--){
		cout << "Case #" << caso++ << ": ";
		cin >> str;
		int left = 5000, right = 5001;
		char resp[10000];
		resp[left] = str[0];
		for(int i = 1; i < str.size(); i++){
			if(str[i] < resp[left]){
				resp[right++] = str[i];
			}
			else{
				left--;
				resp[left] = str[i];
			}
		}
		for(int i = left; i < right; i++)cout << resp[i];
			cout << '\n';
	}
	return 0;
}