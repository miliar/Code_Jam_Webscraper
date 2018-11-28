#include <iostream>
using namespace std;
int main(){
	int t;
	cin >> t;
	for (int ti=0;ti<t;ti++){
		int n;
		cin >> n;
		char c;
		//cin >> c;
		int now=0,cnt=0;
		for (int i=0;i<=n;i++){
			cin >> c;
			int x=c-'0';
			if (x!=0 && now<i){
				cnt+=i-now;
				now=i;
			}
			now+=x;
		}
		cout << "Case #" << ti+1 << ": " << cnt << endl;
	}
	return 0;
}