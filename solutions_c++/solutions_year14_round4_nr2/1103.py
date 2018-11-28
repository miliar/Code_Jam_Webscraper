
#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;
int N,a[1024];
int ori[1024];
int check(){
	int i = 0;
	for(;i<N - 1;i++){
		if(a[i] > a[i + 1]){
			break;
		}
	}
	if(i == N - 2)return 1;
	for(; i < N - 1; i++){
		if(a[i] < a[i + 1]){
			return 0;
		}
	}
	return 1;
}
int main(){
	int T;
	scanf("%d",&T);
	for(int ca = 1; ca <=T ;ca++){
		scanf("%d",&N);
		for(int i=0;i<N;i++){
			scanf("%d", &a[i]);
			ori[i] = a[i];
		}

		sort(a,a + N);
		int ans = N * N;
		do {
			if(check() == 1){
				int tmp[1024];
				for(int i=0;i<N;i++){
					for(int j=0;j<N;j++){
						if(ori[i] == a[j]){
							tmp[i] = j;
						}
					}
				}
				int tmp_ans = 0;
				for(int i=0;i<N;i++){
					for(int j=0;j<N - 1;j++){
						if(tmp[j] > tmp[j + 1]){
							int t = tmp[j];
							tmp[j] = tmp[j + 1];
							tmp[j + 1] = t;
							tmp_ans++;
						}
					}
				}
				ans = min(tmp_ans,ans);
			}
		} while ( std::next_permutation(a , a + N) );



		printf("Case #%d: ",ca);
		printf("%d\n",ans);
	}
	return 0;
}
