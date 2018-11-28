#include<cstdio>
#include<algorithm>
#include<iostream>
#include<vector>
#include<queue>
#include<string>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define N 1100
using namespace std;

int t,n,mn,tab[2][N],wyn;

int main(){
    scanf("%d",&t);
    for(int ttt=1;ttt<=t;ttt++){
        wyn=0;
        scanf("%d",&n);
        for(int i=0;i<n;i++) scanf("%d",&tab[0][i]);
        for(int i=0;i<n-1;i++){
            mn=0;
            for(int j=1;j<n-i;j++) if(tab[i%2][j]<tab[i%2][mn]) mn=j;
            wyn+=min(mn,n-i-mn-1);
            for(int j=0;j<n-i-1;j++) tab[1-i%2][j]=tab[i%2][j+(j>=mn)];
        }
        printf("Case #%d: %d\n",ttt,wyn);
    }
}

