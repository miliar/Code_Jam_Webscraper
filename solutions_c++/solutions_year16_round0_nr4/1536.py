#include <bits/stdc++.h>

using namespace std;


int main(int argc,char *argv[]){
//	freopen("in.txt" , "r" , stdin );
//	freopen("out.txt" , "w" , stdout );
	int Case,cas=0;
	scanf("%d",&Case);
	while(Case--){
		int k , c , s ;
		scanf("%d%d%d",&k,&c,&s);
		printf("Case #%d:",++cas);
		if( c * s < k ) printf(" IMPOSSIBLE\n");
		else for(int i = 1 ; i <= s ; ++ i) printf(" %d" , i);
		printf("\n");
	}
	return 0;
}