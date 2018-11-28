#include <bits/stdc++.h>
#define r(x) scanf("%d",&x)
#define rl(x) scanf("%lld",&x)
using namespace std;
int a[1000];
 
 int getmaxpos(){
 	int maxpos = 0;
 	for(int i=1;i<1000;++i){
 		maxpos = a[maxpos] <a[i] ? i: maxpos;
	 }
	 return maxpos;
 }

int main(){
	long long testcase, i, j,count;

	r(testcase);
	for(i=1;i<=testcase;++i){
		memset(a,0,sizeof(a));
		r(count);
		for(j = 0;j<count;++j){
			r(a['A'+j]);
		}
		printf("Case #%d: ",i);
		if(count==2){
			int pos1;
			int pos2;
			while(a[pos1]>a[pos2]){
				printf("%c ",pos1);
				a[pos1]--;
			}
			while(a[pos2]>a[pos1]){
				printf("%c ",pos2);
				a[pos2]--;
			}
			while(a[pos1]>0){
				printf("%c%c",pos1,pos2);
				a[pos1]--;
				a[pos2]--;
			}
		}
		while(1){
			int pos1 = getmaxpos();
			if(pos1==0) break;
			a[pos1]--;
			int pos2 = getmaxpos();
			a[pos2]--;
			int pos3 = getmaxpos();
			if(a[pos1]==0 && a[pos2]==0 && a[pos3]==1 && pos1 != pos2){
				printf("%c ",pos3);
				a[pos1]++;
				a[pos2]++;
				a[pos3]--;
			}
			else{
				printf("%c%c ",pos1,pos2);
			}
		}
		printf("\n");
	}
	

	return 0;
}
