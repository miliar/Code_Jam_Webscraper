#include <bits/stdc++.h>
using namespace std;
long long tcs, tc, n, nt;
set<char> vst;
int main(){
	scanf("%lli", &tcs);
	for(tc=1;tc<=tcs;tc++){
		scanf("%lli", &n);
		nt = n;
		vst.clear();
		if(n==0) { printf("Case #%lli: INSOMNIA\n", tc); continue; }
		while(true){
			//printf("%lli: ", n);
			char buf[1005];
			sprintf(buf, "%lli", n);
			for(int i=0;i<strlen(buf);i++){
				vst.insert(buf[i]);
			}
			if(vst.size() == 10) break;
			//printf("%lli\n", vst.size());
			n += nt;
		}
		printf("Case #%lli: %lli\n", tc, n);
	}
}