#include<bits/stdc++.h>

using namespace std;
#define CLR(a,val) memset(a, val, sizeof(a))
#define SZ(V) (LL)V.size()
#define ALL(V) V.begin(),V.end()
#define RALL(V) V.rbegin(),V.rend()
#define FORN(i, n) for(LL i = 0; i < n; i++)
#define FORAB(i, a, b) for(LL i = a; i <= b; i++)
#define MOD 1000000007LL
#define PB push_back
#define MP make_pair
#define F first
#define S second

typedef long long LL;
typedef pair<LL,LL> pll;


int main()
{
	LL test;
	cin >> test;
	FORAB(t,1,test){
		LL row,k;
		set<LL> st;
		cin >> row;
		FORN(i,4) FORN(j,4){
			cin >> k;
			if(i==row-1) st.insert(k);
		}
		cin >> row;
		LL ct=0,val;
		FORN(i,4) FORN(j,4){
			cin >> k;
			if(i==row-1 && st.count(k)) ct++,val=k;
		}
		printf("Case #%lld: ",t);
		if(ct==0) cout << "Volunteer cheated!" << endl;
		else if(ct>1) cout << "Bad magician!" << endl;
		else cout << val << endl;
	}
	return 0;
}