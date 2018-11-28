#include<bits/stdc++.h>
using namespace std;
int T, stand, value[1005], n, req;
char kek;

int main(){
	freopen("standin.txt","r",stdin);
	freopen("standout.txt","w",stdout);
	scanf("%d\n",&T);
	for(int i=0;i<T;i++){
		scanf("%d ",&n);
		n++;
		for(int j=0;j<n;j++)
			scanf("%c",&kek), value[j] = kek - '0';
		stand = 0;req = 0;
		for(int j=0;j<n;j++){
			if(stand >= j){
				stand += value[j];
				continue;
			}
			req += (j-stand);
			stand = j;
			stand += value[j];
		}
		printf("Case #%d: %d",i+1,req);
		if(i!=T-1)printf("\n");
	}
	return 0;
}
