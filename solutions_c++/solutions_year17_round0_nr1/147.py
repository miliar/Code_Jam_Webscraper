#include <bits/stdc++.h>
#define F first
#define S second
#define X real()
#define Y imag()
using namespace std;
typedef long long ll;
typedef long double ld;

void solve(){
	string s;
	int k;
	cin>>s>>k;
	int v=0;
	for (int i=0;i+k<=(int)s.size();i++){
		if (s[i]=='-'){
			for (int j=i;j<i+k;j++){
				if (s[j]=='-') s[j]='+';
				else s[j]='-';
			}
			v++;
		}
	}
	for (int i=0;i<(int)s.size();i++){
		if (s[i]=='-') {
			cout<<"IMPOSSIBLE"<<endl;
			return;
		}
	}
	cout<<v<<endl;
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int tcs;
	cin>>tcs;
	for (int tc=1;tc<=tcs;tc++){
		cout<<"Case #"<<tc<<": ";
		solve();
	}
}