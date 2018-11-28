#include <iostream>
using namespace std;

int main() {
	int T, n,  cur, ans, temp;
	char c ;
	cin >> T;
	for(int j=1; j<=T; j++){
		cin >> n;
		cur = ans =  0;
		for(int i=0; i<=n; i++){
			cin >> c;
			//cout << (int) c - '0';
			if(i > cur) {
				temp = (i - cur);
				cur += temp;
				ans += temp; 
			}
			cur += (int) c -'0'; 
		}
		cout << "Case #"<< j <<": " << ans <<endl;
	}
	return 0;
}