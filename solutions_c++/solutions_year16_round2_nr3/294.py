#include<cstdio>
#include<vector>
#include<queue>
#include<algorithm>
#include<iostream>
#include<map>
#include<string>
#define MAX_N 2000
using namespace std;

vector<int> graph[MAX_N+1];
queue<int> q;
map<string,int> numone;
map<string,int> numtwo;
int n,n1,n2,m;

int mx[MAX_N+1],my[MAX_N+1];
int lvl[MAX_N+1];
int finlev;

bool bfs(){
    bool res=false;
    int now,sz,target;
    finlev=n+100;
    while(!q.empty()) q.pop();
    for(int i=1;i<=n;i++){
        if(mx[i]<0){
            lvl[i]=0;
            q.push(i);
        }else{
            lvl[i]=finlev;
        }
    }
    while(!q.empty()){
        now=q.front();q.pop();
        //printf("%d %d\n",now,lvl[now]);
        sz=graph[now].size();
        if(lvl[now]>finlev) break;
        for(int i=0;i<sz;i++){
            target=my[graph[now][i]];
            if(target<0){
                finlev=lvl[now];
            }else if(lvl[target]==n+100){
                lvl[target]=lvl[now]+1;
                q.push(target);
            }
        }
    }
    //printf("%d\n",finlev);
    return (finlev<(n+100));
}

int dfs(int now){
    int sz=graph[now].size(),target;
    for(int i=0;i<sz;i++){
        int target=my[graph[now][i]];
        if(target<0){
            my[graph[now][i]]=now;
            mx[now]=graph[now][i];
            return 1;
        }else if(lvl[target]==lvl[now]+1){
            if(dfs(target)){
                my[graph[now][i]]=now;
                mx[now]=graph[now][i];
                return 1;
            }
        }
    }
    lvl[now]=n+100;
    return 0;
}

int hopcroft(){
    int matching=0;
    for(int i=1;i<=MAX_N;i++){
        mx[i]=-1;my[i]=-1;
    }
    while(bfs()){
        for(int i=1;i<=n;i++){
            if(lvl[i]==0) matching+=dfs(i);
        }
        /*
        for(int i=1;i<=n;i++){
            printf("%d ",mx[i]);
        }
        printf("\n");
        */
    }
    return matching;
}

int main(){
    int ia,ib;
    string im1,im2;
    int t,oneid,twoid,result;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin >> t;
    for(int turn=1;turn<=t;turn++){
        cin >> n;
        for(int i=1;i<=n;i++) graph[i].clear();
        numone.clear();
        numtwo.clear();
        n1=0;n2=0;
        oneid=0;twoid=0;
        for(int i=0;i<n;i++){
            cin >> im1 >> im2;
            if(numone.find(im1)==numone.end()){
                numone[im1]=n1++;
            }
            oneid=numone[im1];
            if(numtwo.find(im2)==numtwo.end()){
                numtwo[im2]=n2++;
            }
            twoid=numtwo[im2];
            graph[oneid+1].push_back(twoid+1);
        }
        result=hopcroft();
        printf("Case #%d: %d\n",turn,n-n1-n2+result);
    }
}
