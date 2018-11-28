#include <bits/stdc++.h>

using namespace std;
typedef long long ll;


string solve (int s,int e){
	stringstream res;
	for(int i=s;i<e;i++){
		res <<" "<< to_string(i);
	}
	return res.str();
}

string calc(int k,int c,int s){
	if(k==1)
		return " 1";
	if(c==1){
		if(s<k)
			return " IMPOSSIBLE";
		else{
			return solve(1,k+1);
		}
	}


	if(s<k-1){
		return " IMPOSSIBLE";
	}else{
		return solve(2,k+1);
	}
}


int main(){
	int tc;
	cin >> tc;
	for (int tt = 1; tt <= tc; tt++) {
		int k,c,s;

		cin>>k>>c>>s;
		string res ="";
		res = calc(k,c,s);
		printf("Case #%d:", tt);
		cout<<res<<endl;
	}
}