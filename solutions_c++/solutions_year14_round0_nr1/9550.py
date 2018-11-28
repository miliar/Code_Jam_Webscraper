#include <cstdio>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

void read(bool *P,int R){
	for(int i=1;i<=4;++i){
		for(int j=1;j<=4;++j){
			int t;
			cin >> t;
			if(R==i)P[t] = true;
		}
	}
}

int main(){
	int T;
	cin >> T;
	int iCase = 0;
	while(T--){
		bool A[20],B[20];
		fill(A,A+20,false);
		fill(B,B+20,false);
		int cA;
		scanf("%d",&cA);
		read(A,cA);
		int cB;
		scanf("%d",&cB);
		read(B,cB);
		
		int cnt = 0,last;
		for(int i=1;i<=16;++i)if(A[i]&&B[i]){
			++cnt;
			last = i;
		}
		printf("Case #%d: ",++iCase);
		if( cnt == 0 ){
			printf("Volunteer cheated!\n");
		}
		if(cnt == 1 ){
			printf("%d\n",last);
		}
		if(cnt > 1 ){
			printf("Bad magician!\n");
		}
	}
	return 0;
}
