#include<bits/stdc++.h>
using namespace std;
#define pb push_back
typedef long long ll;

int main(){
	ifstream inp("./dSmall.in");
	ofstream out("./dSmall.out");
	int t;
	inp>>t;
	for(int a=1; a<=t; a++){
		out<<"Case #"<<a<<": ";
		ll k,c,s;
		inp>>k>>c>>s;
		for(ll i=1; i<=k; i++ ){
			out<<i;
			if(i==k)out<<endl;
			else out<<" ";
		}
	}
}