#include <iostream>
using namespace std;

int main(){
	int t;
	cin >> t;
	for(int tc=1; tc<=t; tc++){
		int sm;
		string s;
		cin >> sm >> s;
		int a[sm+1];
		for (int i = 0; i <= sm; ++i)
			a[i] = (int)(s[i]-'0');
		int tot = a[0];
		int extra = 0;
		for (int i = 1; i <= sm; ++i){
			if(i>tot){
				extra += (i-tot);
				tot += (i-tot);
			}
			tot += a[i];
		}
		cout << "Case #" << tc << ": ";
		cout << extra << endl;
	}
	return 0;
}