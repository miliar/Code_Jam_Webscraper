#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <cstdio>
#include <cstring>
using namespace std;

#define debug(x) cerr<<#x<<"="<<(x)<<endl;
#define MOD 1000002013

inline int add(int a, int b){
	a+=b;
	if((unsigned int)a>=MOD)
		a-=MOD;
	return a;
}

inline int sub(int a, int b){
	a-=b;
	if(a<0)
		a+=MOD;
	return a;
}

inline int mul(int a, int b){
	return (long long)a*b%MOD;

}

inline int mul_add(int a, int b, int c){
	return ((long long)a*b+c)%MOD;
}

int N, M, O[1000], E[1000], P[1000];

int cost(int n){
	return n&1 ? mul(n, (n-1)/2) : mul(n/2, n-1);
}

int expected(){
	int res=0;
	for(int i=0; i<M; i++){
		res=mul_add(P[i], cost(E[i]-O[i]), res);
	}
	return res;
}

int actual(){
	pair<int, int> events[2000];
	for(int i=0; i<M; i++){
		events[2*i]=make_pair(O[i], -P[i]);
		events[2*i+1]=make_pair(E[i], P[i]);
	}
	sort(events, events+2*M);
	int res=0;
	map<int, long long> tickets;
	for(int i=0; i<2*M; i++){
		int at=events[i].first;
		if(events[i].second<0)
			tickets[at]+=-events[i].second;
		else{
			long long left=events[i].second;
			while(left>0){
				assert(!tickets.empty());
				map<int, long long>::reverse_iterator it=tickets.rbegin();
				if(it->second==0){
					tickets.erase(it->first);
				}else{
					long long take=min(it->second, left);
					it->second-=take;
					left-=take;
					res=mul_add(take, cost(at-it->first), res);
				}
			}
		}
	}
	return res;
}

int solve(){
	int expect=expected();
	int act=actual();
	return sub(act, expect);
}

int main(){
	int cases;
	string line;
	getline(cin, line);
	istringstream(line)>>cases;
	for(int i=1; i<=cases; i++){
		scanf("%d %d", &N, &M);
		for(int j=0; j<M; j++)
			scanf("%d %d %d", O+j, E+j, P+j);
		cout<<"Case #"<<i<<": "<<solve()<<endl;
	}
	return 0;
}
