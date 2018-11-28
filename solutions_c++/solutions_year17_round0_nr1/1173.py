#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <map>

using namespace std;
typedef long long int LL;
char s[2000];
int x;
int main() {
	int t;
	cin >> t;
	for(int fm=1; fm<=t; fm++){
		cin >> s >> x;
		//cout << s << " " << x << endl;
		int check = 0,n,count=0;
		for(n=0;s[n]!=0;n++);
		for(int i=0;i<n;i++){
			if(s[i] == '-'){
				if(i+x-1 < n){
					for(int j=0;j<x;j++){
						s[i+j] = s[i+j]=='+'? '-':'+';
					}
					count++;
				}
				else {
					check = 1;
				}
			}
		//	cout << s << endl;
		}
		cout << "Case #" << fm << ": ";
		if(check)cout << "IMPOSSIBLE\n";
		else cout << count << "\n";
	}
	return 0;
}