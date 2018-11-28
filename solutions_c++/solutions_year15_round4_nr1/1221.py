#include<cstdio>
#include<iostream>
#include<cstring>
#include<vector>
#include<algorithm>
using namespace std;
char ch[110][110];
vector<int>E[110];
int N,M;
int A[110][110];
int f(int a,int b){return a*M+b;}
bool judge(int y,int x){
    if(y<0||y>=N||x<0||x>=M) return false;
    return true;
}
bool jud[100010];
int S[100010];
int Y[10],X[10];
int main(){
    freopen("ina.in","r",stdin);
    freopen("outa.out","w",stdout);
    Y[0] = 0;X[0] = 1;
    Y[1] = 0;X[1] =-1;
    Y[2] = 1;X[2] = 0;
    Y[3] =-1;X[3] = 0;
    int T;scanf("%d",&T);int tt = 0;
    while(T--){tt++;
        scanf("%d%d",&N,&M);
        for(int i=0;i<N;i++){
            scanf("%s",ch[i]);
            for(int j=0;j<M;j++){
                if(ch[i][j] == '>') A[i][j] = 0;
                else if(ch[i][j] == '<') A[i][j] = 1;
                else if(ch[i][j] == 'v') A[i][j] = 2;
                else if(ch[i][j] == '^') A[i][j] = 3;
                else A[i][j] = 4;
            }
        }
        for(int i=0;i<N*M;i++){
            jud[i] = false;
            S[i] = 0;
            E[i].clear();
        }
        for(int i=0;i<N;i++){
            for(int j=0;j<M;j++){
                if(A[i][j] != 4){
                    int y = i,x = j;
                    int k = A[i][j];
                    do{
                        y += Y[k];x += X[k];
                        if(!judge(y,x)) {
                            jud[f(i,j)] = true;
                            break;
                        }
                    }while(A[y][x] == 4);
                    if(judge(y,x)) {
                        S[f(y,x)]++;
                    }
                }
            }
        }
        bool ju = true;
        int ans = 0;
        for(int i=0;i<N;i++){
            for(int j=0;j<M;j++){
                if(jud[f(i,j)] && S[f(i,j)] == 0){
                    bool jua = false;
                    for(int k=0;k<4;k++){
                        int y = i,x = j;
                        do{
                            y += Y[k];x += X[k];
                            if(!judge(y,x)) {
                                break;
                            }
                        }while(A[y][x] == 4);
                        if(judge(y,x)) {
                            jua = true;
                        }
                    }if(!jua){
                        ju = false;
                    }
                }
                if(jud[f(i,j)]) ans++;
            }
        }printf("Case #%d: ",tt);
        if(!ju){
            printf("IMPOSSIBLE\n");
        }else{
            printf("%d\n",ans);
        }
    }
    return 0;
}
