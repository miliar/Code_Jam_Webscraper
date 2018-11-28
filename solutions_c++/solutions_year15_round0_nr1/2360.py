#include<bits/stdc++.h>
using namespace std;

int main(){
	int N,NN;
	cin >> N;
	NN=N;
	while(N--){
		int n;
		cin >> n;
		char ch;
		int ret=0;
		int tot=0;
		for(int i=0; i<=n; i++){
			if(tot<i){ ret+=(i-tot);
				tot=i;
			}
			cin >> ch;
			int k=(int)ch -'0';
			tot+=k;
		}
		printf("Case #%d: %d\n",NN-N,ret);
	}
}
