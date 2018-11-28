#include <bits/stdc++.h>
 
using namespace std;
 
#define REP(i, n) for(int i=0; i<(n); i++)
#define FOR(i, a, b) for(int i=(a); i<(b); i++)
#define IFOR(i, a, b) for(int i=(a); i>=(b); i--)
#define FORD(i, a, b, c) for(int i=(a); i<(b); i+=(c))
 
#define SS ({int x;scanf("%d", &x);x;})
#define SI(x) ((int)x.size())
#define PB(x) push_back(x)
#define MP(a,b) make_pair(a, b)
#define SORT(a) sort(a.begin(),a.end())
#define ITER(it,a) for(typeof(a.begin()) it = a.begin(); it!=a.end(); it++)
#define ALL(a) a.begin(),a.end()
#define INF 1000000000
#define V vector
#define S string
#define FST first
#define SEC second
typedef V<int> VI;
typedef V<S> VS;
typedef long long LL;
typedef pair<int, int> PII;

int main(){
	map<pair<pair<int, int>, int>, int> m;
	m[MP(MP(1,1),1)] = 1;
	m[MP(MP(1,1),2)] = 0;
	m[MP(MP(1,1),3)] = 0;
	m[MP(MP(1,1),4)] = 0;

	m[MP(MP(1,2),1)] = 1;
	m[MP(MP(1,2),2)] = 1;
	m[MP(MP(1,2),3)] = 0;
	m[MP(MP(1,2),4)] = 0;

	m[MP(MP(1,3),1)] = 1;
	m[MP(MP(1,3),2)] = 0;
	m[MP(MP(1,3),3)] = 0;
	m[MP(MP(1,3),4)] = 0;

	m[MP(MP(1,4),1)] = 1;
	m[MP(MP(1,4),2)] = 1;
	m[MP(MP(1,4),3)] = 0;
	m[MP(MP(1,4),4)] = 0;

	m[MP(MP(2,2),1)] = 1;
	m[MP(MP(2,2),2)] = 1;
	m[MP(MP(2,2),3)] = 0;
	m[MP(MP(2,2),4)] = 0;

	m[MP(MP(2,3),1)] = 1;
	m[MP(MP(2,3),2)] = 1;
	m[MP(MP(2,3),3)] = 1;
	m[MP(MP(2,3),4)] = 0;

	m[MP(MP(2,4),1)] = 1;
	m[MP(MP(2,4),2)] = 1;
	m[MP(MP(2,4),3)] = 0;
	m[MP(MP(2,4),4)] = 0;

	m[MP(MP(3,3),1)] = 1;
	m[MP(MP(3,3),2)] = 0;
	m[MP(MP(3,3),3)] = 1;
	m[MP(MP(3,3),4)] = 0;

	m[MP(MP(3,4),1)] = 1;
	m[MP(MP(3,4),2)] = 1;
	m[MP(MP(3,4),3)] = 1;
	m[MP(MP(3,4),4)] = 1;

	m[MP(MP(4,4),1)] = 1;
	m[MP(MP(4,4),2)] = 1;
	m[MP(MP(4,4),3)] = 0;
	m[MP(MP(4,4),4)] = 1;
	int ite;
	cin>>ite;
	int cc=1;
	while(ite--){
		cout<<"Case #"<<cc++<<": ";
		int k,r,c;
		cin>>k>>r>>c;
		if(r>c) swap(r,c);
		cout<<(m[MP(MP(r,c),k)]?"GABRIEL":"RICHARD") <<endl;
	}
}