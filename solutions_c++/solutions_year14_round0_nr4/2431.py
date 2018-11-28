#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<vector>
#define eps 10e-6
using namespace std;
int main(){
	freopen("Dwar.txt", "r", stdin);
	freopen("Dwarout.txt", "w", stdout);
	int t, sq = 1;
	cin >> t;
	while (t--){
		int n;
		bool kenvis[1001];
		memset(kenvis, false, sizeof(kenvis));
		cin >> n;
		double naomi[1001], ken[1001];
		for (int i = 0; i < n; i++) cin >> naomi[i];
		for (int i = 0; i < n; i++) cin >> ken[i];
		//cout << "test" << endl;
		sort(naomi, naomi + n);
		sort(ken, ken + n);
		bool flag = true;

		//for (int i = 0; i < n; i++) cout << ken[i] << "  " << naomi[i] << endl;
		int war=0;
		for (int i = 0; i < n; i++){
			flag = true;
			for (int j = 0; j < n; j++){
				if (kenvis[j] == false && ken[j]>naomi[i]){
					flag = false;
					//cout << "Visited: " << ken[j] << endl;
					kenvis[j] = true;
					break;
				}
			}
			if (flag == true)
				war++;
		}
		int dwar = 0;
		int j = n - 1;
		memset(kenvis, false, sizeof(kenvis));
		for (int i = 0; i < n; i++){
			for (int j = 0; j < n; j++){
				if (kenvis[j] == false && naomi[i]>ken[j]){
					dwar++;
					kenvis[j] = true;
					break;
				}
			}
		}
		cout<<"Case #"<<sq++<<": " <<dwar<<" " << war << endl;
	}
	return 0;
}