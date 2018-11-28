#include<cstdio>
#include<algorithm>
using namespace std;

int T;

int main(){
    scanf("%d\n", &T);
    for(int i=1; i<=T; i++){
	int ans = 0, m, c=0, csc;
	scanf("%d", &m);
	for(int cs=0; cs<=m; cs++){
	    scanf("%1d", &csc);
	    if(cs>c){
		ans += cs-c;
		c += cs-c;
	    }
	    c += csc;
	}
	printf("Case #%d: %d\n", i, ans);
    }
}
