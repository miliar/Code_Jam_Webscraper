#include <bits/stdc++.h>
#define S 13
using namespace std;
typedef long long LL;
int in(){int x; scanf("%d", &x); return x;}
int dirX[]={1, 0, -1, 0, 1, -1, 1, -1};
int dirY[]={0, 1, 0, -1, 1, -1, -1, 1};
int rX[] = {1, 1, 2, 2, -1, -1, -2, -2};
int rY[] = {2, -2, 1, -1, 2, -2, +1, -1};
///...............Code Starts From Here...............///

int ar[S];

void digitCut(long long x){
    while(x > 0){
        ar[(int)(x%10)] = 1;
        x /= 10;
    }
}

int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int n, t, cs = 0;
    t = in();
    while(t--){
        memset(ar, 0, sizeof(ar));
        n = in();
        printf("Case #%d: ", ++cs);
        if(n == 0){
            puts("INSOMNIA");
            continue;
        }
        int i = 1, snd;
        while(true){
            int cn = 0;
            snd = n*i;
            digitCut((LL)snd);
            for(int i = 0; i < 10; i++)if(ar[i])cn++;
            if(cn == 10){
                printf("%d\n", snd);
                break;
            }
            i++;
        }
    }
    return 0;
}
