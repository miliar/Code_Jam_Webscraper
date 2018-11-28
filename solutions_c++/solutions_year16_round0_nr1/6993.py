#include <bits/stdc++.h>


int getBit(int x){
    int res = 0;
    while (x){
        res |=  1<< (x%10);
        x /= 10;
    }
    return res;
}

int main(){
//    #ifndef ONLINE_JUDGE
//	freopen("A-large.in", "r", stdin);
//	freopen("A-large.out", "w", stdout);
//    #endif

    int T, cas = 1;
    scanf ("%d", &T);
    while (T--){
		printf("Case #%d: ", cas++);
        int n;
        scanf ("%d", &n);
        if (n == 0){
			printf("INSOMNIA\n");
			continue;
        }
        int res = 0, cnt = 0;
        for (int i = 1; ; i++){
            res |= getBit(i * n);
            if (res == 1023){
				cnt = i;
				break;
            }
        }
		printf("%d\n", cnt*n);


    }
    return 0;
}
