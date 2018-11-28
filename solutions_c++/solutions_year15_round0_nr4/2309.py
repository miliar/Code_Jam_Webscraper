#include <iostream>     // std::cout
#include <algorithm>    // std::lower_bound, std::upper_bound, std::sort
#include <vector>       // std::vector
#include <cstdio>
#include <cstring>
typedef long long LL;
using namespace std;

int x,n,m;

bool input(){
    scanf("%d%d%d",&x,&n,&m);
}
void solve(){
    int res=0;
    if(n>m)swap(n,m);
    if(x==1)res=1;
    if(x==2){
        if((n*m)%x!=0)res=0;
        else res=1;
    }
    if(x==3){
        if(m<3||n<2)res=0;
        else res = ((n*m)%x==0);
    }
    if(x==4){
        if((n*m)%x!=0)res=0;
        else if(m<4)res=0;
        else if(n==1)res=0;
        else if(n==2)res=0;
        else if(n==3)res=1;
        else if(n==4)res=1;
    }
    static int cas=1;
    printf("Case #%d: %s\n",cas++,res?"GABRIEL":"RICHARD");
}

int main () {
    int zz=1;
    scanf("%d",&zz);
    while(zz--){
        input();
        solve();
    }
    return 0;
}
/*
011
011

011
110

*/
