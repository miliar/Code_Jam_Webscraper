#include<iostream>
#include<string>
#include<fstream>
using namespace std;
int main(){

	freopen("output.txt", "w", stdout);
	freopen("A-large.in", "r", stdin);
	int n;
	int k = 0;
	cin >> n;
	while (n--){
		int num;
		k++;
		cin >> num;
		string s;
		cin >> s;
		int cont = 0;
		int all = 0;
		for (int i = 0; i <= num; i++){
			if (all < i){
				cont += i - all;
				all += i - all;
			}
			all = all + (int)s[i] - (int)'0';
		}
		cout << "Case #" << k << ": " << cont << endl;
	}
	return 0;
}
