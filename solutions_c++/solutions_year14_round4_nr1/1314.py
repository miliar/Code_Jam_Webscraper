#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

#define forn(i,n) for(int i=0; i<(int)(n); i++)
#define pb push_back

int main(){
	int t; cin>>t;
	forn(tc,t){
		int n, x;
		cin>>n>>x;
		vector<int>v(n);
		forn(i,n)cin>>v[i];
		sort(v.rbegin(), v.rend());
		int pos = v.size();
		pos--;
		int res = 0;
		for(int i=0; i<=pos; i++){
			if(i==pos){res++; break;}
			if(v[i]+v[pos]<=x)pos--;
			res++;
		}
		printf("Case #%d: %d\n", tc+1, res);
	}
}
