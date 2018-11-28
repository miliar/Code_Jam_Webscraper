#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>
#include <limits.h>
#include <math.h>
#include <algorithm>
#include <bitset>
using namespace std;
typedef long long ll;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("alarge.txt","w",stdout);
	int T,Case=1,n;
	for(scanf("%d",&T);Case<=T;Case++){
		scanf("%d",&n);
		printf("Case #%d: ",Case);
		if(n==0){
			puts("INSOMNIA");
			continue;
		}
		bitset<10> bb;
		ll x;
		for(ll i=1;;i++){
			x=i*n;
			while(x){
				bb[x%10]=1;
				x/=10;
			}
			if(bb.count()==10){
				x=i*n;
				break;
			}
		}
		printf("%I64d\n",x);
	}
    return 0;
}

