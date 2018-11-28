#include<stdio.h>
#include<stdlib.h>
int a,b,c;
long long ctr=0;
void tryFill(int l,int r,int bit){
    //if(bit<27)return;
    if( (l>=a ) || ( r>=b ) )return;
    //printf("wtf");

    //printf("%d %d %d\n",l,r,bit);
    if( ( l&r ) >=c)return ;
    //printf("wtf");
    if(bit==-1){
        ++ctr;
        return;
    }
    //printf("wtf");
    //printf("%lld %lld %lld\n",l + ( 1LL << (bit+1))-1,r+ ( 1LL << (bit+1) ) -1,(l&r) + (1LL<<(bit+1))-1);
    if( l + ( 1LL << (bit+1))-1 <a && r+ ( 1LL << (bit+1) ) -1 <b  && ( (l&r) + (1LL<<(bit+1))-1 <c ) ){
        //printf("case all %d %d %d\n",l,r,bit);
        ctr+= (1LL<<(2*(1+bit)));
        //printf("ctr=%d\n",ctr);
        return;
    }
    //printf("wtf");
    for(int i=0;i<2;++i){
        for(int j = 0 ; j < 2 ; ++ j ){
            tryFill(l| (i<<bit),r|(j<<bit),bit-1);
        }
    }
}
void solve(){
    ctr=0;
    scanf("%d %d %d",&a,&b,&c);
    //printf("%d %d %d\n",a,b,c);
    tryFill(0,0,29);
    printf("%lld\n",ctr);
}

int main(){

    freopen("B-large"".in","r",stdin);
    freopen("B-large"".out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i = 1 ; i <=t ; ++ i ){
        printf("Case #%d: ",i);
        solve();
    }
}
