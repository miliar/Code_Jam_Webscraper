#include <bits/stdc++.h>

using namespace std;

int t,r,c;
string s;
char arr[111][111];
int ll[111][111],rr[111][111],uu[111][111],dd[111][111];
int ans,cek;

int main(){
	scanf("%d",&t);
	for (int jj=1; jj<=t; jj++){
		scanf("%d%d",&r,&c);
		for (int i=0; i<r; i++){
			cin >> s;
			for (int j=0; j<c; j++){
				arr[i][j] = s[j];
			}
		}
		memset(ll,0,sizeof ll);
		memset(rr,0,sizeof rr);
		memset(uu,0,sizeof uu);
		memset(dd,0,sizeof dd);
		for (int i=0; i<r; i++){
			for (int j=0; j<c; j++){
				if (arr[i][j] != '.'){
					ll[i][j] = 1;
					break;
				}
			}
			for (int j=c-1; j>=0; j--){
				if (arr[i][j] != '.'){
					rr[i][j] = 1;
					break;
				}
			}
		}
		for (int j=0; j<c; j++){
			for (int i=0; i<r; i++){
				if (arr[i][j] != '.'){
					uu[i][j] = 1;
					break;
				}
			}
			for (int i=r-1; i>=0; i--){
				if (arr[i][j] != '.'){
					dd[i][j] = 1;
					break;
				}
			}
		}
		ans = 0;
		for (int i=0; i<r; i++){
			for (int j=0; j<c; j++){
				cek = 0;
				if (arr[i][j] != '.'){
					if (arr[i][j] == '<' && ll[i][j]){
						cek = 1;
					}
					if (arr[i][j] == '>' && rr[i][j]){
						cek = 1;
					}
					if (arr[i][j] == '^' && uu[i][j]){
						cek = 1;
					}
					if (arr[i][j] == 'v' && dd[i][j]){
						cek = 1;
					}
				}
				if (cek){
					cek = ll[i][j]+rr[i][j]+uu[i][j]+dd[i][j];
					if (cek == 4){
						ans = -1e8;
					} else ans++;
				}
			}
		}
		printf("Case #%d: ",jj);
		if (ans >= 0) printf("%d\n",ans);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}
