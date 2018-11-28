#include <cstdio>
#include <cstdlib>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstring>

#define MAX 1000

using namespace std;

char b[MAX];
int a[MAX];

int main(int argc, char *argv[]){	
	
	int p; scanf("%d\n", &p);
    for( int T=0; T<p; T++ ){
		int x=0,t=0,S=0; scanf("%d", &S); scanf("%s", b); 
		for(int i=0;i<(S+1);i++) a[i] = b[i]-48;
		for(int i=0;i<(S+1);i++){
			if(a[i]==0) continue;
			if(t<i){ x+=(i-t); t+=(i-t); }
			t+=a[i];
		} 
		printf("Case #%d: %d\n", T+1, x);
    }
    return 0;
}
