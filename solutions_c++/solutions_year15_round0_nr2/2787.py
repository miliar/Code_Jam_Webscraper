#include <cstring>
#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;
int main(){
	freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
	int t,ys=0;
	scanf("%d",&t);
	while(t--){
		int n,max=-1;
		scanf("%d",&n);
		int food[n];
		for(int i=0;i<n;i++){
			scanf("%d",&food[i]);
			if(food[i]>max)
				max = food[i];
		}
		int ans = 5000;
		for(int i=1;i<=max;i++){
			int tmp = i;
			for (int j = 0 ; j<n; j++){
				if(food[j]%i==0)
					tmp += food[j]/i-1;
				else
					tmp += food[j]/i;

			}
			if(tmp<ans)
				ans = tmp;
		}
		printf("Case #%d: %d\n",++ys,ans);
	}
	return 0;
}

