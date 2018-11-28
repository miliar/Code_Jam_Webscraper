#include <iostream>
#include <string>
using namespace std;
int main(){
	int t;
	cin >> t;
	for(int i=1;i<=t;i++){
		string s;
		cin >> s;
		cout << "Case #"<<i<<": ";
		string res="";
		int l=(int)s.length();
		res += s[0];
		for(int j=1;j<l;j++){
			if(res[0] >= res[res.length()-1] ){
				if(s[j] >= res[0]){
					res = s[j]+res;
				}
				else{
					res = res + s[j];
				}
			}
			else {
				if(s[j]>=res[0]){
					res = s[j] + res;
				}
				else {
					res = res + s[j];
				}
			}
		}
		cout << res << endl;
	}
	return 0;
}
