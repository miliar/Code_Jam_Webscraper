#include <cstdio>

using namespace std;
#define ll long long

int main(){
	freopen( "A-large.in", "r", stdin );
	freopen( "A-large.out", "w", stdout );

	int t,i,r,sm,j,k,q;
	char c;


	scanf("%d ",&t);
	for(i=1;i<=t;i++){
		r=0;
		q=0;
		scanf("%d ",&k);
		for(j=1;j<=k+1;j++){
			c=getchar();
			q+=c-48;
			if(q<j){
				r+=(j-q);
				q=j;
			}
		}
		printf("Case #%d: %d\n",i,r);
	}
}