#include <bits/stdc++.h>
using namespace std;
#define x first
#define y second
#define pb push_back
typedef long long ll;
typedef pair<int,int>ii;
typedef long double ld;
typedef vector<int>vi;
typedef pair<ll,ll>pt;
int main(){
	string s,t;
	int test;
	cin>>test;
	for(int te=0;te<test;te++){
		cin>>s;
		int n=s.size();
		t="";t+=s[0];
		for(int i=1;i<n;i++){
			if(s[i]<t[0])t+=s[i];
			else t=s[i]+t;
		}
		cout<<"Case #"<<te+1<<": "<<t<<endl;
	}
	return 0;
}
