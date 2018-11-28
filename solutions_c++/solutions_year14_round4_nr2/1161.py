#include <bits/stdc++.h>
using namespace std;
 
int n,num[1002],ori[1002];

int calc(){
	int copy[1002],i,j,ans=0,now;
	for( i=0 ; i<n ; i++ ){
		copy[i]=ori[i];
	}
	
	for( i=0 ; i<n ; i++ ){
		now=num[i];
		for( j=i ; copy[j]!=now ; j++ );
		
//		printf("%d %d\n",copy[i],now);;
		
		for(; j>i ; j-- ){
			swap(copy[j],copy[j-1]);	
			ans++;
		}	
	}
	return ans;
}

int main(){

	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small-attempt1loll.out","w",stdout);
	int test,ans,i,j,tc=1,temp;
	
	for( scanf("%d",&test) ; test-- ; printf("Case #%d: %d\n",tc++,ans) ){
		scanf("%d",&n);
		ans=2000000000;
		
		for( i=0 ; i<n ; i++ ){
			scanf("%d",&num[i]);
			ori[i]=num[i];
		}
		
		sort(num,num+n);
		do{
			for( i=1 ; i<n && num[i]>num[i-1] ; i++ );
			for(; i<n && num[i]<num[i-1] ; i++ );
			
			if( i!=n ) continue;
			
			ans = min(ans,calc());
			
	/*		if( calc()==7 ){
				for( i=0 ; i<n ; i++ ) printf("%d ",num[i]);
				puts("");	
			}
			*/
			
		}while(next_permutation(num,num+n));
		
	}
	
	return 0;
}

