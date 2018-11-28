#include <vector>
#include <string>
#include <map>
#include <set>
#include <stack>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include "test.h"

using namespace std;
#define For(i,n) for(int i=0;i<n;i++)
#define sz(i) int(i.size())
#define mst(i,n) memset(i,n,sizeof(i))
#define eps 1e-4
#define MOD 1000000007
#define LL long long
#define pi acos(-1)
#define ALL(n) n.begin(),n.end()
#define pb push_back
#define iFor(i,n) for(typeof(n.begin()) i=n.begin();i!=n.end();i++)

int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	int t;
	cin >> t;
	int ca = 0;
	while(t--){
		int r;
		int mem[17] = {};
		cin >> r;
		For(i,4){
			For(j,4){
				int a;
				cin >> a;
				if(i==r-1)
					mem[a] = 1;
			}
		}
		cin >> r;
		int b = 0, ans = 0;
		For(i,4){
			For(j,4){
				int a;
				cin >> a;
				if(i==r-1 && mem[a])
					b += 1, ans = a;
			}
		}
		if(!b) printf("Case #%d: Volunteer cheated!\n", ++ca);
		else if(b == 1) printf("Case #%d: %d\n", ++ca, ans);
		else printf("Case #%d: Bad magician!\n", ++ca);
	}
}
