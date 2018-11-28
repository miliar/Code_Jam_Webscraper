#include<stdio.h>
#include<stdlib.h>
#include<set>
#include<vector>
#include<algorithm>
#include<map>
#include<string.h>
using namespace std;


bool possible[1<<16];
bool nxt[1<<16];
int N=16;
int ctr=0;
int cntBit(int k){
    int ret=0;
    while(k){
        ret++;
        k-=k&(-k);
    }
    return ret;
}
void solve(){
    ctr=0;
    int n;
    scanf("%d",&n);
    for(int i = 0 ; i< (1<<N);++i)possible[i]=1;

    map<int,int> mp ;
    for(int i = 0 ; i < n ; ++ i ){
        memset(nxt,0,sizeof(nxt));
        char tmp[5];
        int id;
        scanf("%s %d",tmp,&id);
        if(id!=0){
            if(mp.count(id))id=mp[id];
            else {
                mp[id]=++ctr;
                id=mp[id];
            }
        }
        //printf("id = %d\n",id);
        if(id==0){
            if(tmp[0]=='E'){
                for(int bit = 0 ; bit < (1<<N) ; bit ++ ){
                    if(possible[bit]){
                        for(int k=0;k<N;++k){
                            if( (bit&(1<<k) )  == 0 ){
                                nxt[bit|(1<<k)]=1;
                            }
                        }
                    }
                }
            }
            else{
                for(int bit = 0 ; bit < (1<<N) ; bit ++ ){
                    if(possible[bit]){
                        for(int k=0;k<N;++k){
                            if( (bit&(1<<k) )  >0 ){
                                nxt[bit-(1<<k)]=1;
                            }
                        }
                    }
                }
            }
        }
        else{
            if(tmp[0]=='E'){
                for(int bit = 0 ; bit < (1<<N) ; bit ++ ){
                    if(possible[bit]){
                        if( (bit&(1<<id) )  == 0 ){
                            nxt[bit|(1<<id)]=1;
                        }

                    }
                }
            }
            else{
                for(int bit = 0 ; bit < (1<<N) ; bit ++ ){
                    if(possible[bit]){
                        if( (bit&(1<<id) )  >0 ){
                            nxt[bit-(1<<id)]=1;
                        }

                    }
                }
            }
        }
        for(int bit = 0 ; bit < (1<<N) ; bit ++ )possible[bit]=nxt[bit];
    }
    int ans=1000;
    for(int i = 0 ; i < (1<<N) ; ++ i ){
        if (possible[i]){
            ans=min(ans,cntBit(i));
        }
    }
    if(ans==1000){
        printf("CRIME TIME\n");
    }
    else
    printf("%d\n",ans);
}

int main(){
    freopen("C-small-attempt1"".in","r",stdin);
    freopen("C-small-attempt1"".out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i = 1 ; i <= t ; ++ i ){
        printf("Case #%d: ",i);
        solve();
    }
}
