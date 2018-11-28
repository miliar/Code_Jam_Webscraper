#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
using namespace std;
#define ll long long
#define ld long double
#define vi vector<int>
#define pb push_back
#define pii pair<int,int>
#define mp make_pair
#define st first
#define nd second
#define mini(a,b) a=min(a,(b))
#define maxi(a,b) a=max(a,(b))
#define RE(i,n) for(int i=0,_n=(n);i<_n;++i)
#define RI(i,n) for(int i=1,_n=(n);i<=_n;++i)
const int inf=1e9+5, nax=1e5+5;

multiset<int> s;
multiset<int> :: iterator it;

int Test() {
	int res = 0;
	int n, W;
	cin >> n >> W;
	RE(i, n) {
		int a;
		cin >> a;
		s.insert(a);
	}
	while(!s.empty()) {
		it = s.end();
		it--;
		int a = *it;
		s.erase(it);
		it = s.upper_bound(W - a);
		if(it != s.begin()) {
			it--;
			s.erase(it);
		}
		res++;
	}
	s.clear();
	return res;
}

int main()
{
	ios_base::sync_with_stdio(0);
	
	int z;
	cin >> z;
	RI(i, z) {
		cout << "Case #" << i << ": " << Test() << "\n";
	}
	
	return 0;
}
