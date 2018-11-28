#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int sum[1010];

int main() 
{
	int T,n,ans;
	string s;
	while(cin >> T) {
		for (int cas = 1; cas<=T; cas++) {
			ans = 0;
			cout<< "Case #"<<cas<<": ";
			cin >> n >> s;
			sum[0] = s[0]-'0';
			for (int i = 1; i<=n; i++) {
				sum[i] = sum[i-1]+s[i]-'0';
			}
			for(int i = 1; i<=n; i++) {
				if(sum[i-1]+ans<i)
					ans++;
			}
			cout<<ans<<endl;
		}
	}
	return 0;
}
