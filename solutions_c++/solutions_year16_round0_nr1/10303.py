#include <stdio.h>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
#include <cstring>
#include <string>
#include <limits.h>
#include <set>

#define sci(a) scanf("%d",&a)
#define scl(a) scanf("%lld",&a)
#define scc(a) scanf("%c",&a)
#define scf(a) scanf("%f",&a)
#define scd(a) scanf("%lf",&a)
#define scs(a) scanf("%s",&a)
#define pri(a) printf("%d",a)
#define prl(a) printf("%lld",a)
#define prc(a) printf("%c",a)
#define prf(a) printf("%f",a)
#define prd(a) printf("%lf",a)
#define prs(a) printf("%s",a)
#define loop(i,a,n) for(int i=a;i<n;++i)
#define nl printf("\n");

#define M 1000000007
#define ll long long int
using namespace std;

int main(){
	int t;
	ll n;
	freopen("abc.txt", "r", stdin);
	freopen("abc1.txt", "w", stdout);
	sci(t);
	loop(c,1,t+1){
		ll arr[11] = { 0 };
		scl(n);
		ll i = 1;
		int p = 0;
		if (n == 0){
			printf("Case #%d: INSOMNIA\n", c);
			continue;
		}
		ll ans = 0;
		while (1){
			ll temp = n*i;
			ll u = temp;
			while (temp > 0){
				ll rem = temp % 10;
				temp = temp / 10;
				arr[rem] = 1;
			}
			loop(i, 0, 10){
				if (arr[i] == 1){
					p = 1;
				}
				else{
					p = 0;
					break;
				}
			}
			if (p == 1){
				ans = u;
				break;
			}
			i++;
		}
		printf("Case #%d: %lld\n", c, ans);
	}

	return 0;
}