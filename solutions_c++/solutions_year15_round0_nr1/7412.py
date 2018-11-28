#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>
#include<stack>
#include<cstdio>
using namespace std;

int main() {

	int T,S,i;
	string arr;
	cin>>T;
	int k=1;
	while(T--) {
		cin>>S;
		cin>>arr;
		int prev=0,cnt,ans=0;
		for(int i=0;i<=S;i++) {
			cnt=arr[i]-'0';
			if(prev<i) {
				ans++;
				prev++;
			}
			prev+=cnt;
		}
		cout<<"Case #"<<k<<": "<<ans<<endl;
		k++;
	}
	return 0;
}
