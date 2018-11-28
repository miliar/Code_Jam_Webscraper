#include <stdio.h>
#include <string.h>

int main(){

	int test,c=1,i,j,x,y;
	int pic[105][105],temp[105][105],max; 
	bool ans;
	
	for( scanf("%d",&test) ; test-- ; printf("Case #%d: %s\n",c++,ans?"YES":"NO") ){
		scanf("%d%d",&x,&y);
		for( i=0 ; i<x ; i++ ){
			max=0;
			for( j=0 ; j<y ; j++ ){
				scanf("%d",&pic[i][j]);
				if( pic[i][j]>max ) max=pic[i][j];
			}
			for( j=0 ; j<y ; j++ ) temp[i][j]=max;
		}
		for( i=0 ; i<y ; i++ ){
			max=0;
			for( j=0 ; j<x ; j++ ) if( pic[j][i]>max ) max=pic[j][i];
			for( j=0 ; j<x ; j++ ) if( temp[j][i]>max ) temp[j][i]=max;
		}
		ans=true;
		for( i=0 ; ans && i<x ; i++ ){
			for( j=0 ; j<y ; j++ )
				if( pic[i][j]!=temp[i][j] ) ans=0;
		}
	}

	return 0;
}

