#include <iostream>
#include <algorithm>
#include <set>
#include <algorithm>
#include <queue>

#define EPS 1e-7

using namespace std;
typedef long long ll;


ll naomi[1010], ken[1010], n;

int solveNaomi(ll *a, ll *b){
	set<ll> sB;
	priority_queue<ll> sA;
	
	for(int i = 0; i < n; i++){
		sA.push(a[i]);
		sB.insert(b[i]);
	}
	ll ans = 0;
	while(!sA.empty()){
		int amt = sA.top(); sA.pop();
		set<ll>::iterator itB = lower_bound(sB.begin(),sB.end(),amt);
		
		if(itB == sB.begin()) break;
		
		sB.erase(*(--itB));
		ans++;
	}
	return ans;
}

int solveKen(ll *a, ll *b){
	set<ll> sB;
	priority_queue<ll> sA;
	
	for(int i = 0; i < n; i++){
		sA.push(a[i]);
		sB.insert(b[i]);
	}
	ll ans = 0;
	while(!sA.empty()){
		int amt = sA.top(); sA.pop();
		set<ll>::iterator itB = lower_bound(sB.begin(),sB.end(),amt);
		if(itB == sB.end()){
			sB.erase(sB.begin());
			ans++;
		}
		else{
			sB.erase(*itB);
		}
	}
	return ans;
	
}

int main(){
	ios_base::sync_with_stdio(false);
	double mass;
	int T;
	cin >> T;
	for(int caso = 1; caso <= T; caso++){
		
		cin >> n;
		for(int i = 0; i < n; i++){
			cin >> mass;
			naomi[i] = (mass+EPS)*100000;
		}
		
		for(int i = 0; i < n; i++){
			cin >> mass;
			ken[i] = (mass+EPS)*100000;
		}
		
		cout << "Case #" << caso << ": " << solveNaomi(naomi,ken) << ' ' << solveKen(naomi,ken) << '\n';
	}
}
