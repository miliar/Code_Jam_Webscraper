#include<cstdio>
#include<cstdlib>
#include<vector>
#include<string>
#include<iostream>
#define MAXN 12
#define IDP 0
#define IDR 1
#define IDS 2
using namespace std;


string v[MAXN+5][(1<<MAXN)+5];
int T, N, R, P, S;

int gt(int a, int b){
    if((a==P && b==R) || (a==R && b==S) || (a==S && b==P)) return true;
    return false;
}

void cnt(int n, int i, int *arr){
    char ch[(1<<MAXN)+5];
    for (int j = v[n][i].size()-1; j>=0; j--){
        if(v[n][i][j] == 'P') arr[IDP]++;
        if(v[n][i][j] == 'R') arr[IDR]++;
        if(v[n][i][j] == 'S') arr[IDS]++;
    }
}

int main(){
    v[0][0] = "P";
    v[0][1] = "R";
    v[0][2] = "S";
    for(int i=1;i<=MAXN;i++){
        int L = (1<<i);
        v[i][0] = v[i-1][0]+v[i-1][1];
        v[i][1] = v[i-1][0]+v[i-1][2];
        v[i][2] = v[i-1][1]+v[i-1][2];
        //cout << v[i][0] << " " << v[i][1] << " " <<v[i][2] << endl;
    }
    scanf("%d", &T);
    for(int t=1;t<=T;t++){
        scanf("%d%d%d%d", &N, &R, &P, &S);
        int haveAns = 0;
        for(int i=0;i<3;i++){
            int arr[3]={0};
            cnt(N, i, arr);
            //printf("%d %d: %d %d %d\n", N, i, arr[0], arr[1], arr[2]);
            if(arr[IDR]==R && arr[IDP]==P && arr[IDS]==S){
                haveAns = 1;
                cout << "Case #" << t << ": " << v[N][i] << endl;
                break;
            }
        }
        if(haveAns == 0) cout << "Case #" << t << ": IMPOSSIBLE" << endl;
    }

    return 0;
}
