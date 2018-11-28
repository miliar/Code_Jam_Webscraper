#include <iostream>
using namespace std;
const int MAXM = 10002;
int main() {
	int T;
	cin>>T;
	int sum[MAXM];
	int s;
	char input[MAXM];
	for (int i=1;i<=T;i++) {
		cin>>s>>input;
		int ans = 0;
		for (int j=0;j<=s;j++) {
			int cur = input[j]-'0';
			sum[j] = (j==0)? cur:sum[j-1]+cur;
			if (j!=0 && j-sum[j-1]>ans) {
				ans = j-sum[j-1];
			}
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
}