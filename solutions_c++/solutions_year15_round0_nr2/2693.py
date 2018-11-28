#include <bits/stdc++.h>
using namespace std;

int bs(int th, int nm){
	int s = 1, e = nm, m, r, v, ret;
	while(s <= e){
		m = (s+e)/2;		
		v = nm/m;
		r = (nm%m)?1:0;
		if(v+r>th){
			s = m+1;
		}
		else{
			ret = m;
			e = m-1;
		}
	}
	return ret-1;
}

int main(){
	int tc, n, a, ar[1005];
	scanf("%d",&tc);
	for(int x = 1; x <= tc; x++){
		printf("Case #%d: ", x);	
		scanf("%d",&n);
		for(int i = 0; i < n; i++) scanf("%d", &ar[i]);
		sort(ar,ar+n);
		reverse(ar,ar+n);
		int ans = 1<<20, csum;
		for(int i = 1; i <= 1000; i++){
			csum = 0;
			for(int j = 0; j < n; j++)
				if(ar[j] > i) csum += bs(i, ar[j]);
			ans = min(ans,csum+i);
		}		
		printf("%d\n", ans);
	}
	return 0;
}

