#include <bits/stdc++.h>
using namespace std;
int main(){
	int t,n,x;
	cin>>t;
	for(int T=1;T<=t;T++){
		cin>>n;
		int v[n];
		int m=0;
		for(int i=0;i<n;i++){
			cin>>v[i];
			m=max(m,v[i]);
		}
		int men=m;
		for(int x=1;x<=m;x++){
			int c=0;
			for(int i=0;i<n;i++){
				if(v[i]>x){
					double q = double(v[i])/double(x);
					q=ceil(q);
					c+=q-1;
				}				
			}
			men=min(x+c,men);
		}
		printf("Case #%d: %d\n",T,men );	

	}
	return 0;
}
