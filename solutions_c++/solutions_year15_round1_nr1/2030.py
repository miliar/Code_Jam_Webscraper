#include<bits/stdc++.h>
using namespace std;

int m[1111];

int main(){
	int T, N;
	scanf("%d", &T);
	for(int caso=1; caso<=T; caso++){
		scanf("%d", &N);
		for(int i=0; i<N; i++){
			scanf("%d", &m[i]);
		}
		
		int tx2=0, resp2=0, resp1=0;
		for(int i=1; i<N; i++){
			if(m[i]<m[i-1]){
				tx2 = max(tx2, m[i-1]-m[i]);
				resp1 += m[i-1]-m[i];
			}
		}
		for(int i=0; i<N-1; i++){
			resp2 += min(tx2, m[i]);
		}
		
		printf("Case #%d: %d %d\n", caso, resp1, resp2);
	}
	return 0;
}

