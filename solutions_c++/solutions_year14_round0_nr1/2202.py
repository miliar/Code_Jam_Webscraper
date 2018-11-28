#include <stdio.h>
#include <string.h>
#include <cstdlib>
#include <map>
#include <set>
#include <string>
using namespace std;
static int t,a,b,c[4][4],d[4][4],save[4],tt=1,sol;
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	while(t--){
		scanf("%d",&a);
		for(int i=0;i<4;++i) {
			for(int j=0;j<4;++j){
				scanf("%d",&c[i][j]);
			}
		}
		scanf("%d",&b);
		for(int i=0;i<4;++i) {
			for(int j=0;j<4;++j){
				scanf("%d",&d[i][j]);
			}
		}
		for(int i=0;i<4;++i) save[i]=c[a-1][i];
		int cnt=0;
		for(int i=0;i<4;++i){
			for(int j=0;j<4;++j){
				if(save[j]==d[b-1][i]) {sol=d[b-1][i];cnt++;}
			}
		}
	    if(cnt==1) printf("Case #%d: %d\n",tt,sol);
		else if(cnt>1) printf("Case #%d: Bad magician!\n",tt);
		else printf("Case #%d: Volunteer cheated!\n",tt);
		++tt;
	}


	return 0;
}