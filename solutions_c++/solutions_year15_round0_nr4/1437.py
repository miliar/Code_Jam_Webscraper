#include<bits/stdc++.h>
 
using namespace std;

int main(){
	#ifndef ONLINE_JUDGE
		freopen("in.txt","r",stdin);
		freopen("out.txt","w",stdout);
	#endif
	int T;
	scanf("%d",&T);
	
	int a[7] = { 0 , 1 , 1 , 2 , 2 , 3 , 3 };
	
	for( int i = 1 ; i<=T ; i++ ){
		int X,R,C;
		scanf("%d%d%d",&X,&R,&C);
		//printf("%d %d %d\n",X,R,C);
		if( X >= 7 ){
			printf("Case #%d: RICHARD\n",i);
			continue;
		}
		else if( X == 1 ){
			printf("Case #%d: GABRIEL\n",i);
			continue;
		}
		else if( X == 2 ){
			if( R&1 && C&1 ){
				printf("Case #%d: RICHARD\n",i);
			}
			else{
				printf("Case #%d: GABRIEL\n",i);
			}
			continue;
		}
		int temp = R*C;
		if( temp % X == 0 ){
			if( min( R , C ) < a[X] ){
				printf("Case #%d: RICHARD\n",i);
			}
			else if( min( R,C ) <= 3 && ( X == 5 || X == 6 ) ){
				printf("Case #%d: RICHARD\n",i);
			}
			else if( min( R,C ) <= 2 && X == 4 ){
				printf("Case #%d: RICHARD\n",i);
			}
			else{
				printf("Case #%d: GABRIEL\n",i);
			}
		}
		else{
			printf("Case #%d: RICHARD\n",i);	
		}
	}
	return 0;
}       
