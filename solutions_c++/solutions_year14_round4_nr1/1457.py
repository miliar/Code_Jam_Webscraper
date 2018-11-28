#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <cmath>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef unsigned long long ul;
typedef pair<int,int> ii;
typedef pair<ll,ll> pll;
typedef vector<ii> vii;

ul one = 1;

int t,n,x,d,c;
int arr[10010];
int ans;

int main(){
	scanf("%d",&t);
	for (int jj=1; jj<=t; jj++){
		scanf("%d%d",&n,&x);
		for (int i=0; i<n; i++){
			scanf("%d",&arr[i]);
		}
		sort(arr,arr+n);
		ans = 0;
		d = n-1;
		c = 0;
		for (;;){
			if (c > d) break;
			if (c == d){
				ans++;
				break;
			}
			if (arr[c] + arr[d] <= x){
				c++;
				d--;
				ans++;
			} else {
				d--;
				ans++;
			}
		}
		printf("Case #%d: %d\n",jj,ans);
	}
	return 0;
}
