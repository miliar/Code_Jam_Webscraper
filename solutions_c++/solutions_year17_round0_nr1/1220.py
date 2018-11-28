#include <bits/stdc++.h>

int main(){
	
	int test,t,n,i,j,len,ans;
	char kek[1004];
	
	scanf("%d",&test);
	
	for( t=0 ; t<test ;){
		ans=0;
		scanf("%s%d",kek,&n);
		len = strlen(kek);
		for( i=0 ; i+n <= len ; i++ ){
			if( kek[i]=='-' ){
				for( j=0 ; j<n ; j++ ) kek[i+j] ^= '+'^'-';	
				ans++;
			}
		}
		
		for(; i<len ; i++ ) if( kek[i]=='-') ans=-1;
		printf("Case #%d: ",++t);	
		
		if( ~ans ) printf("%d\n",ans);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}

