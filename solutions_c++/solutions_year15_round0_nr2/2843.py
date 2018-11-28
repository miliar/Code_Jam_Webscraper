#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>
#include <utility>
#include <map>
#include <vector>
#include <set>

#define mk make_pair
#define pb push_back
typedef  long long  LL;

using namespace std;

int main(){
	int T;
	scanf("%d",&T);
	for(int pp=1;pp<=T;pp++){
		int n,x;
		scanf("%d",&n);
		vector<int> q;
		for(int i=1;i<=n;i++){
			scanf("%d",&x);
			q.pb(x);
		}
		int ans = 99999999;
		int tmp,cot;
		for(int i=1;i<=1000;i++){
			tmp = i;
			for(int k=0;k<n;k++){
				int sz= q[k];
				tmp+= (q[k]%i) ? (q[k]/i+1) : q[k]/i;
				tmp--;
			}
			ans=ans>tmp ? tmp : ans;
		}

		printf("Case #%d: %d\n",pp,ans);
	}
	
	return 0;
}