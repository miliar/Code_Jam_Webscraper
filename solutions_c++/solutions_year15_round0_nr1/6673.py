#include<iostream>
#include<algorithm>
using namespace std;
int main(){
	int T;
	cin>>T;
	for(int t = 1;t <= T;t++){
		int m;
		cin>>m;
		string s;
		cin>>s;

		cout<<"Case #"<<t<<": ";

		int ans = 0;
		for(int i = 0;i < 10;i++){
			int now = i;
			bool flg = true;
			for(int j = 0;j <= m;j++){
				if(now < j && s[j] != '0'){
					flg = false;
					break;
				}
				now += s[j] - '0';
			}
			if(!flg)continue;
			ans = i;
			break;
		}
		cout<<ans<<endl;
	}
}