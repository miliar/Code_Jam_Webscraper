#include<stdio.h>
#include<math.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<set>
#include<iostream>
#include<map>
#include<queue>
#include<bitset>
#include<string>
#include<stdlib.h>
#include<sstream>
#define pb push_back
using namespace std;
#define SIZE 2010
int cs;
int tt,A[SIZE],B[SIZE],dp[SIZE],deg[SIZE],an[SIZE],used[SIZE];
vector<int>e[SIZE];
int fill(int x){
    int bfs[SIZE],i,j,k,ha[SIZE]={},No=1,cnt=0;
    bfs[0]=x;
    ha[x]=1;
    for(i=0,j=1;i<j;i++){
        for(k=0;k<e[bfs[i]].size();k++){
            if(ha[e[bfs[i]][k]])continue;
            if(!an[e[bfs[i]][k]])cnt++;
            bfs[j++]=e[bfs[i]][k];
            ha[bfs[j-1]]=1;
        }
    }
    cnt++;
    for(i=1;cnt;i++){
        if(used[i]==tt)continue;
        else cnt--;
    }
    i--;
    used[i]=tt;
    return i;
    No=max(No,j);
    while(used[No]==tt)No++;
    used[No]=tt;
    return No;
}
int main(){
    int T,i,j,k,N;
    scanf("%d",&T);
    while(T--){
        memset(an,0,sizeof(an));
        tt++;
        cin>>N;
        for(i=1;i<=N;i++)e[i].clear();
        for(i=1;i<=N;i++){
            cin>>A[i];
        }
        int bb=0;
        for(i=1;i<=N;i++){
            if(A[i]!=1)e[i].pb(dp[A[i]-1]);
            //for(j=1;j<A[i];j++)e[i].pb(dp[j]);
            if(A[i]>bb){
                bb=A[i];
            }
            else{
                e[dp[A[i]]].pb(i);
                //for(j=A[i];j<=bb;j++)e[dp[j]].pb(i);
            }
            dp[A[i]]=i;
        }
        for(i=1;i<=N;i++){
            cin>>B[i];
        }
        bb=0;
        for(i=N;i>0;i--){
            if(B[i]!=1)e[i].pb(dp[B[i]-1]);
            //for(j=1;j<B[i];j++)e[i].pb(dp[j]);
            if(B[i]>bb){
                bb=B[i];
            }
            else{
                e[dp[B[i]]].pb(i);
                //for(j=B[i];j<=bb;j++)e[dp[j]].pb(i);
            }
            dp[B[i]]=i;
        }
        for(i=1;i<=N;i++){
            an[i]=fill(i);
        }
        /*
        for(i=1;i<=N;i++,puts("")){
            printf("[%d]:",i);
            for(j=0;j<e[i].size();j++)printf("%d,",e[i][j]);
        }
        */
        printf("Case #%d:",++cs);
        for(i=1;i<=N;i++)printf(" %d",an[i]);
        puts("");
        bb=0;
        for(i=1;i<=N;i++){
            int ma=1;
            for(j=1;j<i;j++){
                if(an[i]>an[j])ma=max(ma,A[j]+1);
            }
            if(A[i]!=ma)fprintf(stderr,"error on case %d\n",cs);
        }
    }
    return 0;
}

