#include <cstdio>
#include <algorithm>
using namespace std;

int t,d;
int p[1010];

int check(int m){
	int count = 0;
	for(int i = d-1; i >= 0; i--){
		if(p[i] > m) count += (p[i]-1)/m;
		else break;
	}
	return count;
}

int main(){
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	for(int k = 1; k <= t; k++){
		scanf("%d",&d);
		for(int i = 0; i < d; i++) scanf("%d",&p[i]);
		sort(p,p+d);
		int minVal = 9999999;
		for(int i = 1; i <= p[d-1]; i++){
			minVal = min(minVal,check(i)+i);
		}
		printf("Case #%d: %d\n",k,minVal);
	}
}