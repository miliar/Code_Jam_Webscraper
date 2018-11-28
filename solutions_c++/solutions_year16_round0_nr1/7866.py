#define _CRT_SECURE_NO_WARNINGS 
#include <iostream>
#include<string>

using namespace std;

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++){
		int a[10] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
		int col = 0;
		int n;
		cin >> n;
		if (n == 0){
			cout << "Case #" << i << ": INSOMNIA" << '\n';
		}
		else{
			int kf = 1; 
			while (col != 10){
				string s = to_string(n * kf);
				for (int c = 0; c < s.size(); c++){
					int r = s[c] - '0';
					if (a[r] == 0){
						a[r] = 1;
						col++;
					}
				}
				kf++;
			}
			kf--;
			cout << "Case #" << i << ": " << (n * kf) << '\n';
		}
	}
	return 0;
}
