#include<bits/stdc++.h>

using namespace std;

#define pb push_back
#define ll long long

int n;

string toString(int x){
	
	string ret = "";
	for(int i = 0; i < n-2; i++){
		ret += ('0' + x%2);
		x/=2;
	}
	reverse(ret.begin(),ret.end());
	return ret;

}

ll tobase(string st, ll x){
	ll ret = 0;
	ll base = 1;
	for(int i = st.size() - 1; i >=0; i--){
		ret+= (st[i]-'0')*base;
		base*=x;
	}
	return ret;
}

ll test(ll x){
	for(ll i = 2; i <= min((ll)sqrt(x),10000LL); i++){
		if(x%i==0) return i;
	}
	return -1;
}

int main(){
	
	freopen("out.txt","w",stdout);
	int m = 0;
	scanf("%d %d",&n ,&m);
	
	cout<<"Case #1:\n";
	
	for(int i = 0; i <(1<<(n-2)) && m!=0; i++){
		
		string st = "1";
		st += toString(i);
		st+= "1";
		
		
		bool can =true;
		
		vector <ll> v;
		
		for(int i = 2; i <=10; i++){
			ll inbase = tobase(st, i);
		//	cout<<inbase<<endl;
			v.pb(test(inbase));
			if(v.back() == -1) can= false;
		}
		
		
		if(!can) continue;
		;
		
		m--;
		
		cout<<st;
		for(int i = 0; i < 9; i++){
			printf(" %lld" ,v[i]);
		}
		printf("\n");
		
	}
	
}
