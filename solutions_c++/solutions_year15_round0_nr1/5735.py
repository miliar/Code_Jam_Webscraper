#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
using namespace std;
typedef long long ll;
#define DEBUG
#define mod 1000000007

int main(){
	ios::sync_with_stdio(false);
	#ifdef DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	#endif // DEBUG
	
	int T,SM;
	cin>>T;
	string s;
	for(int t=1;t<=T;t++){
		cin>>SM;
		cin>>s;
		ll ans=0, count=0;
		for(int i=0;i<=SM;i++){
			if(s[i]!='0'){
				if(count>=i){
					count += (ll)(s[i]-'0');
				}
				else{
					ll temp = (ll)i-count;
					count += (temp) + (ll)(s[i]-'0');
					ans += temp;
				}
			}
		}
		cout<<"Case #"<<t<<": ";
		cout<<ans<<endl;
	}

	return 0;
}
