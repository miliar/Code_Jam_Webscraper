#include <algorithm>
#include <stdio.h>
#include <vector>
using namespace std;

int T[4][4] = {
		{1,2,3,4},
		{2,-1,4,-3},
		{3,-4,-1,2},
		{4,3,-2,-1}
	};

int calc(int a,int b){
	//printf("%d",abs(a));
	//return T[3][3];
	if(a==0) return b;
	if((a>0 && b>0)||(a<0 && b<0))
	return T[abs(a)-1][abs(b)-1];
	return T[abs(a)-1][abs(b)-1]*(-1);
}

int main(){
	int N,L,mul,cur;
	bool flag1, flag2;
	char c;
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("out", "w", stdout);
	scanf("%d",&N);
	for(int i=0; i<N; i++){
		cur = 0;
		flag1 = flag2 = false;
		printf("Case #%d: ",i+1);
		scanf("%d",&L);
		scanf("%d",&mul);
		vector<int> ls(L,0);
		scanf("%c",&c);
		for(int j=0; j<L; j++){
			scanf("%c",&c);
			//c = 'i';
			switch(c){
				case 'i':
					ls[j] = 2;
					break;
				case 'j':
					ls[j] = 3;
					break;
				case 'k':
					ls[j] = 4;
			}
		}
		for(int k=0; k<mul; k++){
			for(int j=0; j<L; j++){
				cur = calc(cur,ls[j]);
				if(!flag1 && cur == 2){
					flag1 = true;
					cur = 0;
				}
				else if(flag1 && !flag2 && cur == 3){
					flag2 = true;
					cur = 0;
				}
			}
		}
		if(flag1 && flag2 && cur == 4){
			printf("YES\n");
		}
		else printf("NO\n");
	}
	return 0;
}