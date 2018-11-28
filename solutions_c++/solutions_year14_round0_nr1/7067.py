#include<iostream>
#include<vector>
#include<map>
#include<stdio.h>
using namespace std;
int matrix[5][5];
int main(){
	int test,ans1,ans2;
	vector < int > v2;
	map <int,int> m;
	scanf("%d",&test);
	int t = 1;
	while( test-- ) {
		scanf("%d",&ans1);
		for( int i=1; i<=4; i++ ) {
			for( int j=1; j<=4; j++ ) {
				scanf("%d",&matrix[i][j]);
				if ( i == ans1 ) {
					m[ matrix[i][j] ]++;
				}
			}
		}
		scanf("%d",&ans2);
		for( int i=1; i<=4; i++ ) {
			for( int j=1; j<=4; j++ ) {
				scanf("%d",&matrix[i][j]);
				if ( i == ans2 )
					v2.push_back(matrix[i][j]);
			}
		}
		int count=0,answer=0;
		for ( int i=0; i<4; i++) {
			 if ( m[v2[i]] ) {
				 count++;
				 answer=v2[i];
			 }
		}
		switch (count) {
			case 0:
				printf("Case #%d: Volunteer cheated!\n",t);
				break;
			case 1:
				printf("Case #%d: %d\n",t,answer);
				break;
			default:
				printf("Case #%d: Bad magician!\n",t);
				break;
		}
		v2.clear();m.clear();
		t++;
	}
	return 0;
}
