#include<string>
#include<iostream>
using namespace std;
int main(){
	int t, n; string s;
	cin >> t;
	for(int z = 1;  z <= t; ++ z){
		cin >> n >> s;
		int cnt = s[0] - '0', ret = 0;
		for(int i = 1; i <= n; ++ i){
			if(cnt < i){
				ret += i - cnt;
				cnt = i;
			}
			cnt += s[i] - '0';
		}
		cout << "Case #" << z << ": " << ret << endl;
	}
	return 0;
}