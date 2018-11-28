#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <cassert>

using namespace std;

typedef pair<int,int> P;
typedef pair<P,int> Q;

const int MXX = 509*109*2;
int Y,X;
bool M[509][109];
vector<vector<Q> > G;

int mx[] = {0,1};
int my[] = {1,0};
int MOVES = 2;
int SRC,SNK;

int bfs_ford_fulkerson(){
    queue<int> q;
    vector<P> padre(SNK+1,P(-1,-1));

    int x,y,xi,yi,c;
    q.push(SRC);
    while(!q.empty() and padre[SNK].first == -1){
        x = q.front();q.pop();

        // printf("%d\n",x);

        for(int i=G[x].size()-1;i>=0;i--){
            y = G[x][i].first.first;
            c = G[x][i].second;

            if(c > 0 and padre[y].first == -1){
                padre[y] = P(x,i);
                q.push(y);
            }
        }
    }

    if(padre[SNK].first==-1)
        return 0;
    else{
        y=SNK;//Buscando la capacidad residual minima
        x=padre[y].first;
        while(y!=SRC){//Antes era padre[y]!=ini pero puede haber ciclos
            xi = padre[y].second;
            yi = G[x][xi].first.second;

            assert(G[x][xi].first.first == y);
            assert(G[y][yi].first.first == x);

            G[x][xi].second--;
            G[y][yi].second++;

            y=x;
            x=padre[x].first;
        }
        return 1;
    }
}

void add(int x,int y,int cc){
    int idx = G[x].size();
    int idy = G[y].size();
    G[x].push_back(Q(P(y,idy),cc));
    G[y].push_back(Q(P(x,idx),0));//!

    // printf("%d -> %d = %d\n",x,y,cc);
}

int inn(int x){return 2*x;}
int out(int x){return inn(x)+1;}

int solve(){
    memset(M,false,sizeof(M));
    int N=1;
    int xa=0,ya=0,xb=0,yb=0;
    scanf("%d %d %d",&X,&Y,&N);

    for(int i=1;i<=N;i++){
        scanf("%d %d %d %d",&xa,&ya,&xb,&yb);
        for(int b=ya;b<=yb;b++)
            for(int a=xa;a<=xb;a++)
                M[b][a] = true;
    }
    SRC = Y * X * 2;
    SNK = SRC + 1;

    G.clear();
    G.resize(SNK+1);

    int id,idy;
    int ii,jj;
    // printf(">> %d %d\n",X,Y);
    for(int i=0;i<Y;i++){
        for(int j=0;j<X;j++){
            if(M[i][j])continue;
            id = X*i+j;

            add(inn(id),out(id),1);

            if(i == 0){
                add(SRC,inn(id),1);
            }
            if(i == Y-1){
                add(out(id),SNK,1);
            }

            for(int k=0;k<MOVES;k++){
                ii = i + my[k];
                jj = j + mx[k];

                if(ii<0 or jj<0 or ii>=Y or jj>=X)continue;
                idy = X*ii+jj;
                if(M[ii][jj] == false){
                    add(out(id),inn(idy),1);
                    add(out(idy),inn(id),1);
                }
            }
        }
    }

    int flow=0;
    while(bfs_ford_fulkerson())flow++;
    return flow;
}

int main(){
    int NC;scanf("%d",&NC);
    for(int i=1;i<=NC;i++){
        int ans = solve();
        printf("Case #%d: %d\n",i,ans);
    }
}