#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#define ll long long
using namespace std;
ll T,A,B;

bool check(ll sq) {
	char digits[101];
	int len=0;

	while(sq) {
		digits[len++]='0'+sq%10;
		sq/=10;
	}

	bool ok=true;
	int half = len/2;

	for(int i=0;i<half;i++)
		if(digits[i]!=digits[len-1-i]) {
			ok=false;
			break;
		}

	return ok;
}

int main() {

	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);

	scanf("%d",&T);

	for(int c=1;c<=T;c++) {
		scanf("%lld %lld", &A,&B);

		ll a=A/2;
		while(a*a>=A) a--;
		ll cnt = 0;
		a++;
		while(a*a<=B) {
			ll sq = a*a;
			if(check(a) && check(sq)) { 
				cnt++;
			}
			a++;
		}

		printf("Case \#%d: %ld\n", c, cnt);
	}

}