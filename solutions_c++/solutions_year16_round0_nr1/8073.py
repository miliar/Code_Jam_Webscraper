#include <bits/stdc++.h>
using namespace std;

bool used[10];
int main(){

	freopen("readtest.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t,n;
	scanf("%d", &t);
	while(t--){
		memset(used,0,sizeof used);
		scanf("%d", &n);
		int temp= n;
		int ans= 0;
		static int test= 1;
		if( !n){
			printf("Case #%d: INSOMNIA\n",test++);
			continue;
		}
		while(temp){
			if( !used[temp % 10])
				ans++;
			used[temp % 10]= true;
			temp/= 10;
		}
		int i= 2;
		long long x,z= 1;
		while(ans < 10){
			temp= i * z * n;
			x= temp;
			while(temp){
				if( !used[temp % 10])
					ans++;
				used[temp % 10]= true;
				temp/= 10;
			}
			i++;
		}
		printf("Case #%d: %I64d\n",test++,x);
	}

	return 0;
}
