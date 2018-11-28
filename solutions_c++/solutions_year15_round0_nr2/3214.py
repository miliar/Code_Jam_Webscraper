#include <iostream>
#include <vector>
#include <string>
#include <bitset>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <cmath>
#include <cstdio>
#define infin 2147483647
#define pb push_back
#define rs resize
#define mp make_pair
#define sz(x) int((x).size())
#define vv(x) vector<vector<x> >
#define all(x) (x).begin(), (x).end()
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;

int main(){
	int tests;
	cin>>tests;
	for(int t=0; t<tests; t++){
		int n, at, svar = 1000, br, c;
		cin>>n;
		multiset<int> p;
		for(int i=0; i<n; i++){
			cin>>at;
			p.insert(at);
		}
		for(int i=1; i<=1000; i++){		// alla möjliga brytpunkter
			at = br = 0;
			for(multiset<int>::iterator it = p.begin(); it != p.end(); it++){
				if(*it > i){
					c = ceil(1.0* *it/i);
					at += c - 1;
					// br = max(br, (int)ceil(*it / c));
				}
				// else br = max(br, *it);
			}
			// cout<<i<<' '<<br<<' '<<at<<endl;
			svar = min(svar, i+at);
		}
		printf("Case #%d: %d\n", t+1, svar);
	}
}