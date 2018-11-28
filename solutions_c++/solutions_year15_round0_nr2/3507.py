#include <iostream>
#include <queue>
#include <vector>
#include <set>
#include <unordered_set>
#include <cstdio>

using namespace std;

set<set<int> > us;	

int max(vector<int> v){
	int m = -(1<<30);
	for(auto x: v) m = max(m, x);
	return m;
}

int rec(vector<int> v, int s){
	int x = max(v);
	if(x < 4 || s >10) return s + x;
	//cout << "v: "; for(auto x: v) cout << x << " "; cout << endl;
	int m = 1<<30;
	vector<int> vv = v;
	for(int i = 0; i < v.size(); i++) vv[i]--;
	m = min(m, rec(vv, s+1));

	for(int i = 0; i < v.size(); i++){
		vv.resize(0);
		if(v[i] < 2) continue;
		int a = v[i]/2;
		int b = v[i]/2+v[i]%2;
		for(int j = 0; j < v.size(); j++){
			if(j == i) continue;
			vv.push_back(v[j]);
		}

		vv.push_back(a); vv.push_back(b);
		set<int> ss;
		for(auto x: vv) if(x>0) ss.insert(x);
		if(us.find(ss) != us.end()) continue;
		us.insert(ss);
		m = min(m , rec(vv, s+1));
	}
	return m;
}

int solve3(){
	us.clear();
	int n, x, s=0;
	vector<int> v;
	cin >> n;
	for(int i = 0; i < n; i++){
		cin >> x;
		v.push_back(x);
	}
	return rec(v,0);

}



int solve2(){
	int n, m = -1, x;
	cin >> n;
	vector<int> v;
	for(int i = 0; i < n; i++){
		cin >> x;
		v.push_back(x);
		m = max(m, x);
	}
	
	for(int i = 2; i < m; i++){
		int y = 0;
		for(int j = 0; j < v.size(); j++){
			y += (v[j]-1)/i;
		}
		m = min(m , y + i);
	}
	return m;
}

int solve(){
	int n, x, s=0, m = 1<<29;
	priority_queue<int> pq;
	cin >> n;
	for(int i = 0; i < n; i++){
		cin >> x;
		pq.push(x);
	}
	while(pq.top() > 1){
		x = pq.top();

	/*	priority_queue<int> p = pq;
		cout << "p1: "; while(!p.empty()){
			cout << p.top() << " ";
			p.pop();
		} cout << endl;*/

		m = min(m, s + x);
		pq.pop();
		pq.push(x/2 + x%2);
		pq.push(x/2);
	//	cout << x << " " << m << " " << s << endl;
		s++;
	}
	m = min(m, pq.top()+s);
	return m;
}

int main(){
	int T;
	cin >> T;
	for(int i = 0; i < T; i++) cout << "Case #" << i+1 << ": " << solve2() << endl;
	return 0;
}