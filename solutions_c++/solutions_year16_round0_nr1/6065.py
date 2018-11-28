#include <bits/stdc++.h>
using namespace std;

void main2(){
	int n; cin >> n;
	if (n == 0){
		cout << "INSOMNIA" << endl;
		return;
	}
	vector<bool> mark(10,false);
	int cnt = 0;
	for (int i=n; true; i+=n){
		int cur = i;
		while (cur){
			int d = cur % 10;
			if (mark[d] == false){
				mark[d] = true;
				cnt++;
			}
			cur/=10;
		}
		if (cnt == 10){
			cout << i << endl;
			break;
		}
	}
}

int main(){
	int t; cin >> t;
	for (int o=1; o<=t; o++){
		cout << "Case #" << o << ": ";
		main2();
	}
	return 0;
}
