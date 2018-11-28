#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
#include <cstdio>
#include <string>
using namespace std;
typedef struct Q{
	char c;
	int i;
	Q(char cc,int ii) {c=cc;i=ii;}
	Q() {c=0;i=0;}
} Q;
struct comp {
	bool operator()(Q a,Q b) {
		return a.i < b.i;
	}
};
void solve()
{
	priority_queue<Q,vector<Q>,comp> pq;
	int nn,t; cin >> nn;
	int n = 0;
	for( int i = 0 ; i < nn ; i++ )
	{
		cin >> t; n+=t;
		pq.push( Q('A'+i,t) );
	}
	Q q1;
	vector<string> v;
	string s;
	while(true)
	{
		if(n==3) break;
		s.clear();
		if(pq.empty()) break;
		q1 = pq.top(); pq.pop();
		q1.i--; n--;
		s.push_back(q1.c);
		if(q1.i>0) pq.push(q1);
		if(pq.empty()) {
			v.push_back(s);
			break;
		}
		q1 = pq.top(); pq.pop();
		q1.i--; n--;
		if(q1.i>0) pq.push(q1);
		s.push_back(q1.c);
		v.push_back(s);
	}
	if(n==3)
	{
		s.clear();
		q1 = pq.top(); pq.pop();
		q1.i--; n--;
		if(q1.i>0) pq.push(q1);
		s.push_back(q1.c);
		v.push_back(s);
		
		s.clear();
		q1 = pq.top(); pq.pop();
		q1.i--; n--;
		if(q1.i>0) pq.push(q1);
		s.push_back(q1.c);
		q1 = pq.top(); pq.pop();
		q1.i--; n--;
		if(q1.i>0) pq.push(q1);
		s.push_back(q1.c);
		v.push_back(s);
	}
	for( int i = 0 ; i < (int)v.size() ; i++ ) cout << v[i] << " ";
	cout << endl;
	return;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t; cin>>t;
	for( int i = 1 ; i <= t ; i++ )
	{
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}