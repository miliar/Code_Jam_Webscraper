#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long int ulli;
typedef long long int lli;
#define pb push_back
#define ft first
#define se second
#define mp make_pair

void printVector(vector<int> v){
	for(int i = 0; i < v.size(); i++){
		cout << v[i];
		if(i != v.size() - 1) cout << " ";
	}
}

void printResult(string res, vector<int> v){
	cout << res << " ";
	printVector(v);
	cout << endl;
}

string intialise(){
	string res = "";
	for(int i = 0; i < 32; i++) res.push_back('0');
	res[0] = res[31] = '1';
	return res;
}

int main(){
	int t;
	cin >> t;
	int n, j;
	cin >> n >> j;
	vector<int> v;
	for(int i = 2; i <= 10; i++) v.push_back(i + 1);
	if(n == 32 && j == 500){
		int count = 0;
		cout << "Case #1: \n";
		string res = intialise();
		printResult(res, v);
		count++;
		for(int i = 1; i < 31; i++){
			for(int j = i + 1; j < 31; j += 2){
				res = intialise();
				res[i] = res[j] = '1';
				printResult(res, v);
				count++;
			}
		}
		for(int i = 1; i < 31; i++){
			for(int j = i + 1; j < 31; j += 2){
				for(int p = j + 1; p < 31; p ++){
					for(int q = p + 1; q < 31; q += 2){
						res = intialise();
						res[i] = res[j] = res[p] = res[q] = '1';
						printResult(res, v);
						count++;
						if(count == 500) return 0;
					}
				}
			}
		}
	}

}