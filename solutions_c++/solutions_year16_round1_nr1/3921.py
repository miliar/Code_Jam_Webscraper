#include <bits/stdc++.h>
#define REP(a,b,c) for(int a=b;a<c;a++) 
#define pb push_back 
#define mp make_pair 
#define sz(v) (int)v.size()
#define debug(x) cout << #x << ":" << x << endl;
using namespace std;

deque<char> cola;

void sort(string s){
	queue<char> scol;
	REP(i,0,sz(s)){
		scol.push(s[i]);
	}
	cola.pb(scol.front());
	scol.pop();
	while(!scol.empty()){
		if(scol.front()<cola.front()) cola.pb(scol.front());
		else cola.push_front(scol.front());
		scol.pop();
	}
	return;
}

int main(){
	int t,tam;
	int cont=1;
	string s;
	cin>>t;
	REP(i,0,t){
		s.clear();
		cola.clear();
		cin>>s;
		sort(s);
		tam=sz(cola);
		cout<<"Case #"<<cont<<": ";
		while(!cola.empty()){
			cout<<cola.front();
			cola.pop_front();
		}
		cont++;
		cout<<endl;
	}
	return 0;
}
