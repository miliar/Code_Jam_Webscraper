#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int N, a[1000];
int main(){
	int TN, ca=0, i, m1, m2, maxx, j;
	scanf("%d", &TN);
	while(TN--){
		scanf("%d", &N);
		maxx=0;
		for(i=0;i<N;i++){
			scanf("%d", &a[i]);
			maxx=max(maxx, a[i]);
		}

		m1=0;
		for(i=1;i<N;i++){
			if(a[i]<a[i-1]){
				m1+=a[i-1]-a[i];
			}
		}

		int gap=0;
		for(i=1;i<N;i++){
			gap=max(gap, a[i-1]-a[i]);
		}
		m2=0;
		for(i=1;i<N;i++){
			if(a[i-1]>=gap){
				m2+=gap;
			}
			else{
				m2+=min(a[i-1], gap);
			}
		}
		printf("Case #%d: %d %d\n", ++ca, m1, m2);
	}
	return 0;
}