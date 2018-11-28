#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>

using namespace std;

void printar(vector<bool> ar){
	for(bool i : ar)
		cout << i << ", ";
	cout << endl;
}

void problem(int n){
	if(n == 0){
		cout << "INSOMNIA" << endl;
		return;
	}
	
	vector<bool> seen;
	for(int i = 0; i < 10; i++)
		seen.push_back(false);
	
	bool flag = true;
	int curnum = n, mult = 0;
	while(flag){
		mult++;
		curnum = mult * n;	
		while(curnum != 0){
			seen[curnum % 10] = true;
			curnum /= 10;
		}
		
		flag = false;
		for(auto b : seen)
			if(b == false)
				flag = true;
	}
	cout << mult * n << endl;
}

int main(){
	freopen("A-large.in", "r", stdin); freopen("A-large.out", "w", stdout);
	int n;
	cin >> n;
	
	int N;
	for(int i = 0; i < n; i++){
		cin >> N;
		cout << "Case #" << i + 1 << ": ";
		problem(N);
	}
}