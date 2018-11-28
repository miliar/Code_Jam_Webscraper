#include <iostream>
#include <string>
using namespace std;
int dbg = 1;
 
int main() {
	int n; cin >> n;
	//if(dbg) cout << n << endl;
 
	for(int i=0;i<n;i++){
		int maxnum; cin >> maxnum;
		string str; cin >> str;
		//if(dbg) cout << "maxnum=" << maxnum << endl;
		//if(dbg) cout << "str=" << str << endl;
 
		int friends=0;
		int standing=0;
		for(int j=0;j<=maxnum;j++){
			if(standing < j){
				friends += j - standing;
				standing = j;
			}
 
			standing += str[j] - 48;
		}
		cout << "Case #" << i+1 << ": " << friends << endl;
	}
 
	return 0;
}