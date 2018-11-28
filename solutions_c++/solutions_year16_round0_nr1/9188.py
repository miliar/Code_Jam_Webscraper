#include <bits/stdc++.h>
#define REP(a,b,c) for(int a=b;a<c;a++) 
#define pb push_back 
#define mp make_pair 
#define sz(v) (int)v.size()
#define debug(x) cout << #x << ":" << x << endl;
using namespace std;

set<int> s;
int ans;
int valor;

void go(int n){
	int dig;
	queue<int> cola;
	cola.push(n);
	while(sz(s)!=10){
		dig=cola.front();
		while(dig!=0){
			if(s.count(dig%10)==0) s.insert(dig%10);
			dig/=10;
			//cout<<sz(s)<<endl;
		}
		cola.pop();
		if(sz(s)==10) break;
		cola.push(n*valor);
		valor++;
	}
	ans=n*(valor-1);
}

int main(){
	int t,n,cont;
	cin>>t;
	cont=1;
	REP(i,0,t){
		valor=2;
		s.clear();
		cin>>n;
		ans=n;
		if(n==0){
			cout<<"Case #"<<cont<<": INSOMNIA"<<endl;
			cont++;
		}
		else{
			go(n);
			cout<<"Case #"<<cont<<": "<<ans<<endl;
			cont++;
		}
	}
	return 0;
}
