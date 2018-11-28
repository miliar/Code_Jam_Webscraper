#include<stdio.h>
#include<iostream>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<stack>
#include<queue>
#include<algorithm>
#define mem(a,b) memset(a,b,sizeof(a))
#define Max(a,b) ((a)>(b)?(a):(b))
#define Min(a,b) ((a)<(b)?(a):(b))
#define INF 0x3f3f3f3f
#define MAX 150

using namespace std;

int map[MAX][MAX];

int l,w;

int judge(int y,int x){
    int i,j;
    int chax = 1,chay = 1;
    for(i = 0;i < w;++ i){
        if(map[i][x] > map[y][x]){
            chay = 0;
        }
    }
    for(i = 0;i < l;++ i){
        if(map[y][i] > map[y][x]){
            chax = 0;
        }
    }
    if(!chax && !chay)
        return 0;
    return 1;
}

int main(){
#ifndef ONLINE_JUDGE
    freopen("G:\\study\\programs\\test\\in.txt","r",stdin);
    freopen("G:\\study\\programs\\test\\out.txt","w",stdout);
#endif
    int num_text;
    int i,j,k = 0,flag;
    scanf("%d",&num_text);
    while(k < num_text){
        flag = 1;
        k ++;
        printf("Case #%d: ",k);
        scanf("%d %d",&w,&l);
        for(i = 0;i < w;++ i){
            for(j = 0;j < l;++ j){
                scanf("%d",&map[i][j]);
            }
        }
        for(i = 0;i < w;++ i){
            for(j = 0;j < l;++ j){
                if(!judge(i,j)){
                    printf("NO\n");
                    flag = 0;
                    break;
                }
            }
            if(!flag) break;
        }
        if(!flag) continue;
        printf("YES\n");
    }
    return 0;
}
