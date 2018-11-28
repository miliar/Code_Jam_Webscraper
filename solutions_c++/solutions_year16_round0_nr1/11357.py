#include<bits/stdc++.h>
using namespace std;
int main() {
	int t=0,i=0;
	scanf("%d",&t);
	while(t!=i){
		set<int> s;
		int n=0,j=1;
		scanf("%d",&n);
		if(n==0){
			i++;
			printf("Case #%d: INSOMNIA\n",i);
		}else{
			int nn=n;
			while(s.size()!=10){
				int ns=j*n;
				nn=ns;
				while(ns>0){
					int rem=ns%10;
					ns=ns/10;
					s.insert(rem);
				}
				j++;
			}
			i++;
			printf("Case #%d: %d\n",i,nn);
		}
	}
	return 0;
}
