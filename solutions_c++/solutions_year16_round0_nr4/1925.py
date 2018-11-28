#include<iostream>
#include<vector>
#include<stack>
#include<string.h>
#include<map>
using namespace std;
int main(){
	int t, c, k, s;
	cin >> t;
	for(int z = 1; z <= t; ++ z){
		cin >> k >> c >> s;
		cout << "Case #" << z << ":";
		for(int i = 0; i < k; ++ i)
			cout << ' ' << i + 1;
		cout << endl;
	}
}