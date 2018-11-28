#include<stdio.h>
int a1,a2;
int tab1[10][10],tab2[10][10];
int check(int k){
	int chk = 0;
	for(int i = 0 ; i < 4 ; i++ ){
		if( tab1[a1][i] == k ) chk = 1;
	}
	if( !chk ) return 0;

	chk = 0;
	for(int i = 0 ;i < 4 ; i++ ){
		if( tab2[a2][i] == k ) chk = 1;
	}
	return chk;
}
int main(){
	int t;
	scanf("%d",&t);
	for(int e = 0; e < t ;e++ ){
		scanf("%d",&a1);
		a1--;
		for(int i = 0 ;i < 4 ; i++ ){
			for(int j = 0;j < 4 ; j++ ){
				scanf("%d",&tab1[i][j]);
				tab1[i][j]--;
			}
		}
		scanf("%d",&a2);
		a2--;
		for(int i = 0 ;i < 4 ; i++ ){
			for(int j = 0;j < 4 ; j++ ){
				scanf("%d",&tab2[i][j]);
				tab2[i][j]--;
			}
		}

		int count = 0;
		int pos = 0;
		for(int i = 0;i < 16 ; i++ ){
			count+=check(i);
			if( check(i) == 1 ) pos = i;
		}
		printf("Case #%d: ",e+1);
		if( count == 1 ) printf("%d\n",pos+1);
		if( count > 1  ) printf("Bad magician!\n");
		if( count == 0 ) printf("Volunteer cheated!\n");
	}
}

