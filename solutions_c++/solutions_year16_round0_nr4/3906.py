#include <bits/stdc++.h>
using namespace std;

void main2(){
	int k,c,s; cin >> k >> c >> s;
	for (int i=1; i<=k; i++)
		cout << i << " ";
	cout << endl;
}

int main(){
	int t; cin >> t;
	for (int o=1; o<=t; o++){
		cout << "Case #" << o << ": ";
		main2();
	}
	return 0;
}
