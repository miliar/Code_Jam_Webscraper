#include <stdio.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	scanf("%d",&t);
	int dt=t;
	while(t--){
	    int a,b,c;
	    printf("Case #%d:",(dt-t));
	    scanf("%d %d %d",&a,&b,&c);
	    for(int i=0;i<c;i++){
	        printf(" %d",(i+1));
	    }
	    printf("\n");
	}
	return 0;
}
