#include <iostream>
#include <cstdio>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <sstream>
#include <fstream>
#include <string>

#define rep(i,n) for(int i=0;i<n;i++)
#define VI vector<int>
#define pb(x) push_back(x)
#define ll long long
#define For(i,a,b) for(int i=a;i<b;i++)
#define sz(s) int(s.size())
using namespace std;

const int maxn = 10100;

int a[maxn];

int main() {
	int t;
	cin >> t;
	rep(g,t){
		int n,x;
		cin >> n >> x;
		rep(i,n)
			cin >> a[i];
		sort(a, a+n);
		reverse(a, a+n);
		int cnt = 0;
		rep(i,n)
			if(a[i] != -1){
				cnt++;
				For(j,i+1,n)
					if(a[j] != -1 && a[j]+a[i] <= x){
						a[j] = -1;
						break;
					}
				a[i] = -1; 
			}
		cout << "Case #" << g+1 << ": " << cnt << endl;
	}
	return 0;
}
