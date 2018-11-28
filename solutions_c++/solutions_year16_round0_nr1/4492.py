#include<iostream>
using namespace std;

int main() {
	int n, N, cnt, ans;
	FILE *fin, *fout;
	fin=fopen("A-large.in", "r");
	fout=fopen("A-large.out", "w");
	//scanf("%d", &n);
	fscanf(fin, "%d", &n);
	for( int i=1; i<=n; ++i ) {
		//scanf("%d", &N);		
		fscanf(fin, "%d", &N);
		//N=i;
		cnt=0;
		int vis[10] = {0};
		if( N==0 ) {
			fprintf(fout, "Case #%d: INSOMNIA\n", i);
		}
		else {
			int k=1;
			while(cnt!=10) {
				ans = k*N;
				k+=1;
				int temp = ans;
				while(temp){
					if( vis[temp%10]==0 ) {
						cnt+=1;
						vis[temp%10]=1;
					}
					temp/=10;
				}
			}
			fprintf(fout, "Case #%d: %d\n", i, ans);
		}
	}
	return 0;
}
