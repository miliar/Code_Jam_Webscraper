#include<cstdio>
using namespace std;

const int MAX = 4096 + 10;

int rec[13][3];

char arr[MAX];
char tt[MAX];

void init(){
    rec[0][0] = 1;
    rec[0][1] = 0;
    rec[0][2] = 0;
    for(int i = 1 ; i < 13 ; i++){
        rec[i][0] = rec[i-1][0] + rec[i-1][2];
        rec[i][1] = rec[i-1][0] + rec[i-1][1];
        rec[i][2] = rec[i-1][1] + rec[i-1][2];
    }
}

char lose(char c){
    if(c == 'P') return 'R';
    if(c == 'R') return 'S';
    if(c == 'S') return 'P';
}

bool ifswap(char *A,  char *B){
    int t = 0;
    while(A[t] && B[t]){
        if(A[t] != B[t]) return A[t] > B[t];
        t++;
    }
    return false;
}

void mysort(char *T, int l, int r){
    int mid = (l+r) / 2;
    if(mid != l){
        mysort(T, l, mid);
        mysort(T, mid+1, r);
    }
    bool goswap = ifswap(T+l, T+mid+1);
    if(goswap){
        for(int i = l ; i <= mid ; i++){
            tt[i] = T[i];
        }
        for(int i = 0 ; i < (r-l+1)/2 ; i++){
            T[l+i] = T[mid+1+i];
        }
        for(int i = 0 ; i < (r-l+1)/2 ; i++){
            T[mid+1+i] = tt[l+i];
        }
    }
}

void gen(char c, int n){
    arr[0] = c;
    int cnt = 1;
    for(int i = 1 ; i <= n ; i++){
        for(int j = cnt - 1 ; j >= 0 ; j--){
            arr[2*j+1] = lose(arr[j]);
            arr[2*j] = arr[j];
        }
        cnt *= 2;
    }
    mysort(arr, 0, cnt-1);
    for(int i = 0 ; i < cnt ; i++)
        printf("%c", arr[i]);
    puts("");
}

int main(){
    init();
    int TN;
    scanf("%d" ,&TN);
    for(int casen = 1 ; casen <= TN ; casen++){
        printf("Case #%d: ", casen);
        int n, r, p, s;
        scanf("%d %d %d %d" ,&n, &r, &p, &s);
        char winner;
        if(p == rec[n][0] && r == rec[n][1] && s == rec[n][2]) winner = 'P';
        else if(p == rec[n][1] && r == rec[n][2] && s == rec[n][0]) winner = 'S';
        else if(p == rec[n][2] && r == rec[n][0] && s == rec[n][1]) winner = 'R';
        else{
            puts("IMPOSSIBLE");
            continue;
        }
        gen(winner, n);
    }
    return 0;
}
