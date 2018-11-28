#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<set>
#include<string.h>
using namespace std;
int P,Q,N;
int mx=0;
struct state{
    vector<pair<int,int> > hp;
    int turn,gold;
    state(vector<pair<int,int> > hpp,int tt,int gg): hp(hpp),turn(tt),gold(gg){}
    bool operator < ( const state & o ) const{
        if(hp!=o.hp)return hp<o.hp;
        if(turn != o.turn)return turn<o.turn;
        if(gold != o.gold)return gold<o.gold;
        return 0;
    }
};
set<state> stt;
void dfs(vector<pair<int,int >  > hp,int turn,int gold){
    // 0 human 1 com
    if(stt.find(state(hp,turn,gold))!=stt.end())return;
    stt.insert(state(hp,turn,gold));
    if(gold>mx)mx=gold;
    if(turn){
        for(int i = 0 ; i < hp.size() ; ++ i ){
            if(hp[i].first>0){
                vector<pair<int,int> > nxt = hp;
                nxt[i].first-=Q;
                dfs(nxt,0,gold);
                return ;
            }
        }
    }
    else{
        dfs(hp,1,gold);
        for(int i = 0 ; i<hp.size() ; ++ i ){
            if(hp[i].first>0){
                vector<pair<int,int> > nxt = hp;
                nxt[i].first-=P;
                int nxtGold=gold;
                if(nxt[i].first<=0)nxtGold+=nxt[i].second;
                dfs(nxt,1,nxtGold);
            }
        }
    }
}

void solve(){
    mx=0;
    stt.clear();
    scanf("%d %d %d",&P,&Q,&N);
    vector<pair<int,int> > hp;
    for(int i = 0 ; i < N ; ++ i ){
        int k,l;
        scanf("%d %d",&k,&l);
        hp.push_back(make_pair(k,l));
    }
    dfs(hp,0,0);
    printf("%d\n",mx);

}

int dp[2000];
int nxt[2000];
void solveLarge(){
    memset(dp,0,sizeof(dp));
    for(int i = 2 ; i<2000 ; ++ i ) dp[i]=-200000000;
    scanf("%d %d %d",&P,&Q,&N);

    for(int i = 0 ; i < N ; ++ i ){
        int h,g;
        scanf("%d %d",&h,&g);
        for(int j = 0 ; j < 2000 ; ++ j ) nxt[j]=-200000000;
        for(int j = 0 ; j <2000;++j){
            // let tower atk for x time
            // then we atk
            for(int x=0;x<=10;++x){
                if(h-x*Q<=0){
                    if(j+x<2000)
                    nxt[j+x]=max(nxt[j+x],dp[j]);
                    break;
                }
                int req = (P-1+ h-x*Q)/P;
                if(j+x-req>=0&&j+x-req<2000)
                    nxt[j+x-req]=max(nxt[j+x-req],dp[j]+g);
            }
        }
        for(int j = 0 ; j<2000;++j)dp[j]=nxt[j];
    }
    int ans = 0 ;
    for(int j = 0 ; j <2000 ; ++ j ){
        ans=max(ans,dp[j]);
    }
    printf("%d\n",ans);


}






int main(){
    freopen("B-large"".in","r",stdin);
    freopen("B-large"".out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i = 1 ; i <= t ; ++ i ){
        printf("Case #%d: ",i);
        solveLarge();
    }
}
