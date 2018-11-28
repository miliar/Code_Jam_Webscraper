#include<bits/stdc++.h>
using namespace std;

int main(){
	int t;
	cin >> t;
	for(int z = 1; z <= t; z++){
		int k,c,s;
		cin >> k >> c >> s;
		printf("Case #%d: ", z);
		for(int i = 0; i < k; i++){
			cout << i+1 << " ";
		}
		cout << endl;
	}
	return 0;
}