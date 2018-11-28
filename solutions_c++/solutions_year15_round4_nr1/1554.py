#include<bits/stdc++.h>
using namespace std;

int main(){
	int T;
	cin>>T;
	for(int t=1; t<=T; t++){
		int N, M;
		cin>>N>>M;
		char brd[N][M];
		for (int i = 0; i < N; ++i)
		{
			for (int j = 0; j < M; ++j)
			{
				cin>>brd[i][j];
			}
		}
		int flag[N][M];
		memset(flag, 0, sizeof(flag));
		long long ans = 0;	
		for (int i = 0; i < N; ++i)
		{
			int mi = M, ma = -1;
			for (int j = 0; j < M; ++j)
			{
				if(brd[i][j] != '.') {
					ma = max(ma, j);
					mi = min(mi, j); 
				}
			}
			if(ma >= 0) flag[i][ma] |= 1;
			if(mi < M) flag[i][mi] |= 2;	
		}
		for (int i = 0; i < M; ++i)
		{
			int mi = N, ma = -1;
			for (int j = 0; j < N; ++j)
			{
				if(brd[j][i] != '.') {
					ma = max(ma, j);
					mi = min(mi, j); 
				}
			}
			if(ma >= 0) flag[ma][i] |= 4;
			if(mi < N) flag[mi][i] |= 8;
		}
		for(int i=0; i<N; i++){
			for(int j=0; j<M; j++){
				if(flag[i][j] == 15) {
					ans = -1;
					break;
				}
				switch(brd[i][j]){
					case '^': {
						if(flag[i][j] & 8) ans++;
						break;
					}
					case 'v': {
						if(flag[i][j] & 4) ans++;
						break;
					}
					case '>': {
						if(flag[i][j] & 1) ans++;
						break;
					}
					case '<': {
						if(flag[i][j] & 2) ans++;
						break;
					}
				}
			}
			if(ans == -1)break;
		}
		if(ans != -1)printf("Case #%d: %lld\n", t, ans);
		else printf("Case #%d: IMPOSSIBLE\n", t);
	}
	return 0;
}
