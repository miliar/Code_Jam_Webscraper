#include <iostream>
#include <string>
using namespace std;

int main(){
	freopen("in.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t;
	cin>>t;
	for(int i = 0; i < t; i++){
		int n;
		string row;
		cin>>n>>row;
		int ans = 0, cnt = 0;
		for(int j = 0; j <= n; j++){
			ans += max(0, j - cnt);
			cnt = max(cnt, j) + row[j] - '0';
		}
		cout<<"Case #"<<i + 1<<": "<<ans<<"\n";
	}
}