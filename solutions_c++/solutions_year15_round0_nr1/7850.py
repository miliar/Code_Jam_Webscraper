#include <iostream>
using namespace std;
int t;
int main(){
	cin >> t;
	for (int i = 0; i < t; ++i){
		int m,total = 0,ans=0;
		string s;
		cin >> m;
		cin >> s;
		total += s[0]-'0';
		for (int j = 1; j < m+1; ++j){
			if(total < j){
				ans += (j-total);
				total+= (j-total);
			}
			total+= s[j]-'0';
		}
		cout << "Case #" << i+1 << ": " << ans << endl;
	}
}