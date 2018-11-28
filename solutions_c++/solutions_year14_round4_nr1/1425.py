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
int a[100005];
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t;
	cin >> t;
	int ca = 0;
	while(t--){
		int n,s;

		cin >> n >> s;
		for(int i=0;i<n;i++) cin >> a[i];
		sort(a, a+n);
		int i = 0, j = n - 1;
		int ans = 0;
		while(i <= j){
		    if(i == j){
                ans ++;
                break;
		    }
            if(a[i] + a[j] <= s){
                i++, j--;
                ans++;
            }
            else{
                j--;
                ans++;
            }
		}
		printf("Case #%d: %d\n", ++ca, ans);
	}
}
