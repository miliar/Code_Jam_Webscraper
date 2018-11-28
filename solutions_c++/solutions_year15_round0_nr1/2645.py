#include<cstdio>
using namespace std;

int main(){
    int T, SMAX;
    char *aud;
    scanf(" %d ", &T);
    for(int t=1; t<=T; ++t){
	scanf(" %d ", &SMAX);
	aud = new char[SMAX+1];
	for(int i=0; i<=SMAX; ++i){
	    scanf("%c", &aud[i]);
	    aud[i] -= 48;
	}
	int res = 0;
	int cur = 0;
	for(int i=0; i<=SMAX; ++i){
	    if(cur >= i){
		cur += aud[i];
	    }else{
		res += (i-cur);
		cur = i+aud[i];
	    }
	}
	printf("Case #%d: %d\n", t, res);
	delete aud;
    }
    return 0;
}
