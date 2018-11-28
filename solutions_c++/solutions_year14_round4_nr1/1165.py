#include <bits/stdc++.h>
using namespace std;

int main(){

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int test,ans,i,j,tc=1;
	int n,d,disc[10002];
	
	for( scanf("%d",&test) ; test-- ; printf("Case #%d: %d\n",tc++,ans) ){
		scanf("%d%d",&n,&d);
		ans=0;
		
		for( i=0 ; i<n ; i++ ) scanf("%d",&disc[i]);
		sort(disc,disc+n);
		
		for( i=0,j=n-1 ; i<=j ; ans++ ){
			if( disc[i]+disc[j]<=d ){
				i++,j--;
			}
			else{
				j--;	
			}
		}
	}
	
	return 0;
}

