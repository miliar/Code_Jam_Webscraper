#include<cstdio>
#include<cstdlib>
using namespace std;

int main(){
    int T, N, cur, cnt, check;
    char ne[10];
    scanf(" %d ", &T);
    for(int t=1; t<=T; ++t){
	scanf(" %d ", &N);
	if(N == 0){
	    printf("Case #%d: INSOMNIA\n", t);
	    continue;
	}
	for(int i=0; i<10; ++i) ne[i] = 0;
	cnt = 1;
	while(true){
	    cur = N*cnt;
	    while(cur > 0){
		ne[cur%10] = 1;
		cur /= 10;
	    }
	    check = 1;
	    for(int i=0; i<10; ++i) check *= ne[i];
	    if(check == 1){
		printf("Case #%d: %d\n", t, N*cnt);
		break;
	    }
	    cnt += 1;
	}
    }
    return 0;
}
