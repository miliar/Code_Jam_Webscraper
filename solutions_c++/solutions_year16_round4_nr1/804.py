#include <bits/stdc++.h>
using namespace std;

#define FOR(i,n) for(int i=0;i<n;++i)


long long all;
// char, p, r
map<pair<int,int>,tuple<int,int,int> > m;

inline tuple<int,int,int> addt(tuple<int,int,int> x,tuple<int,int,int> y) {
	return make_tuple(get<0>(x)+get<0>(y),get<1>(x)+get<1>(y),get<2>(x)+get<2>(y));
}

tuple<int,int,int> possible(int c,int l) {
	if(m.find(make_pair(c,l))!=m.end()) return m[make_pair(c,l)];
	if(l==0) {
		if(c==0) return m[make_pair(c,l)] = make_tuple(1,0,0);
		else if(c==1) return m[make_pair(c,l)] = make_tuple(0,1,0);
		else return m[make_pair(c,l)] = make_tuple(0,0,1);
	}
	if(c==0) {
		auto x = possible(0,l-1);
		auto y = possible(1,l-1);
		return m[make_pair(c,l)] = addt(x,y);
	}
	if(c==1) {
		auto x = possible(1,l-1);
		auto y = possible(2,l-1);
		return m[make_pair(c,l)] = addt(x,y);
	}
	if(c==2) {
		auto x = possible(0,l-1);
		auto y = possible(2,l-1);
		return m[make_pair(c,l)] = addt(x,y);
	}
}

int memo[3][2050];
int chars[3];

void construct(int c,int l) {
	if(l==0) printf("%c",chars[c]);
	else {
		if(c==0) {
			if(memo[0][l-1] < memo[1][l-1]) {
				construct(0,l-1);
				construct(1,l-1);
			}
			else {
				construct(1,l-1);
				construct(0,l-1);
			}
		}
		if(c==1) {
			if(memo[1][l-1] < memo[2][l-1]) {
				construct(1,l-1);
				construct(2,l-1);
			}
			else {
				construct(2,l-1);
				construct(1,l-1);
			}
		}
		if(c==2) {
			if(memo[0][l-1] < memo[2][l-1]) {
				construct(0,l-1);
				construct(2,l-1);
			}
			else {
				construct(2,l-1);
				construct(0,l-1);
			}
		}
		
	}
}
		



		
	
	


	
int main(void) {
	chars[0] = 'P';
	chars[1] = 'R';
	chars[2] = 'S';
	int t;
	scanf("%d",&t);
	for(int tt=1;tt<=t;++tt) {
		int n,r,p,s;
		scanf("%d%d%d%d",&n,&r,&p,&s);
		printf("Case #%d: ",tt);
		
		
		
		
		auto a = possible(0,n);
		auto b = possible(1,n);
		auto c = possible(2,n);
		auto aa = make_tuple(p,r,s);
		if(aa!=a && aa!=b && aa!=c) printf("IMPOSSIBLE\n");
		else {
			memo[0][0] = 0;
			memo[1][0] = 1;
			memo[2][0] = 2;
			
			for(int i=1;i<=n;++i) {
				auto a1 = min(make_pair(memo[0][i-1],memo[1][i-1]),make_pair(memo[1][i-1],memo[0][i-1]));
				auto a2 = min(make_pair(memo[1][i-1],memo[2][i-1]),make_pair(memo[2][i-1],memo[1][i-1]));
				auto a3 = min(make_pair(memo[2][i-1],memo[0][i-1]),make_pair(memo[0][i-1],memo[2][i-1]));
				vector<pair<pair<int,int>,int> > v;
				v.push_back(make_pair(a1,0));
				v.push_back(make_pair(a2,1));
				v.push_back(make_pair(a3,2));
				sort(v.begin(),v.end());
				int pos = 0;
				memo[v[0].second][i] = pos;
				for(int j=1;j<3;++j) {
					if(v[j].first!=v[j-1].first) ++pos;
					memo[v[j].second][i] = pos;
				}
			}
			int best = -1;
			if(aa==a) best = 0;
			if(aa==b && (best==-1 || memo[1][n]<memo[best][n])) best = 1;
			if(aa==c && (best==-1 || memo[2][n]<memo[best][n])) best = 2;
			construct(best,n);
			printf("\n");
		}
		
		
		
		
		
		
		
	}
}