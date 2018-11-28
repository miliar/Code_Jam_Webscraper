#include <iostream>
#include <string>
using namespace std;


int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tests;
	cin >> tests;
	for(int j = 0;j < tests;++j){
		long long n;
		cin >> n;	
		string a;
		long long cur = 0;
		cin >> a;
		long long ans = 0;
		for(long long i = 0;i < a.length();++i){
			if(cur >= i) cur = cur + int(a[i]) - 48;
			else{
				ans = ans + i - cur;
				cur = i;
				cur= cur + a[i] - 48;	
			}	
		}
		cout << "Case #" << j + 1 << ": ";
		cout << ans << "\n";
	}
	return 0;
}