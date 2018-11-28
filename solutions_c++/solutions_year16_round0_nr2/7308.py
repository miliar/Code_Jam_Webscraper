#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long l;
typedef double dbl;
typedef pair<int , int> pll;

#define endl '\n'


ll i , j;

string s;

void op(int len){
	int x;
	for(x=0;x<=len;x++){
		if(s[x] == '-')s[x] = '+';
		else s[x] = '-';
	}
}


int main(){
	freopen("B-large.in" , "r" , stdin);
	freopen("output.txt" , "w" , stdout);
	ios::sync_with_stdio(0);
	int t;cin>>t;
	for(int T = 1 ; T<=t ;T++){
		cin>>s;
		int len = s.length() , ans = 0;
		for(i = len-1 ; i>=0 ; i--){
			if(s[i] == '-'){
				op(i);
				ans++;
			}
		}
		cout<<"Case #"<<T<<": "<<ans<<endl;
	}
	
	return 0;
}
