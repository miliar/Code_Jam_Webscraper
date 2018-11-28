#include <algorithm>
#include <iostream>
#include <vector>
#include <bitset>
#include <stack>
#include <queue>
#include <cmath>
#include <string>
#include <map>
#include <set>
using namespace std;
#include <stdio.h>
#include <memory.h>
const int N = 1000001;
const long long INF = 1ll<<51;
typedef long long ll;

int T,n;
string str;

int main() {
	freopen("A-large.in","r",stdin);
	freopen("ansA.txt","w",stdout);
	scanf("%d",&T);
	for(int t=1;t<=T;++t) {
		cin >> n >> str;
		ll hav=0,need=0;
		hav += (str[0]-'0');
		for(int i=1;i<=n;++i) {
			if(i > hav) {
				need += (i-hav);
				hav += (i-hav);
			}
			hav += (str[i]-'0');
		}
		printf("Case #%d: %lld\n",t,need);
	}
    return 0;
}
