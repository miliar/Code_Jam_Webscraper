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

int t;
int a,n,m,k;
int x[1010],y[1010];
int ans,cl,ans2;

int main(){
	scanf("%d",&t);
	for (int i=3; i<=1000; i++){
		int temp = i-2;
		y[i] = temp*4;
		x[i] = y[i]+(temp*temp);
	}
	for (int jj=1; jj<=t; jj++){
		scanf("%d%d%d",&a,&m,&k);
		n = min(a,m);
		m = max(a,m);
		if (n < 3 || k < 5){
			ans2 = k;
		} else {
			ans2 = 1000000000;
			for (int j=3; j<=n; j++){
				if (j*m < k) continue;
				cl = x[j];
				ans = y[j];
				a = j;
				while (cl < k && a < m){
					cl += j;
					ans += 2;
					a++;
					if (cl - 2 >= k){
						ans--;
						cl -= 2;
					}
				}
				if (cl < k) ans += (k-cl);
				while (cl > k && a > 3){
					if (cl-j >= k){
						ans -= 2;
						cl -= j;
						a--;
					} else if (cl-2 >= k){
						ans--;
						cl -= 2;
						break;
					} else break;
				}
				ans2 = min(ans2,ans);
			}
		}
		printf("Case #%d: %d\n",jj,ans2);
	}
	return 0;
}
