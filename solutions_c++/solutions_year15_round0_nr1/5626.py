#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int tc;
	cin>>tc;
	int count = 1;
	while (tc--) {
		int ans = 0;
		int berdiri = 0;
		int n;
		string s;
		int arr[1001];
		cin>>n>>s;
		for (int i=0;i<s.length();i++) {
			arr[i] = s[i] - '0';
			if (i == 0) berdiri+=arr[i];
			else {
				if (arr[i] > 0) {
					if (berdiri < i) {
						ans += (i-berdiri);
						berdiri = i;
					}
					berdiri+=arr[i];
				}
			} 
		}
		cout<<"Case #"<<count++<<": "<<ans<<endl;
	}
	return 0;
}
