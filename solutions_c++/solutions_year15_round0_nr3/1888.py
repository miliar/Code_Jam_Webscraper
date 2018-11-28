#include <stdio.h>
#include <iostream>
#include <vector>
#include <string.h>
#include <map>
#include <queue>
#include <algorithm>
#include <math.h>
#include <set>

using namespace std;

#define N 100000
#define P 1005
#define INF 1LL<<61
#define LL  long long
#define MOD 1000000007

#define MID ((l + r)/2)
#define lx (x<<1)
#define rx ((x<<1)|1)

struct Item{
    int fuhao;
    char c;
    Item(){}
    Item(int _fuhao,char _c){
        fuhao = _fuhao;
        c = _c;
    }
};

Item mul(Item a,Item b){
    Item c;
    c.fuhao = a.fuhao * b.fuhao;
    if(a.c=='1'){
        c.c = b.c;
    }
    else if(b.c == '1'){
        c.c = a.c;
    }
    else if(a.c == 'i' && b.c == 'i') {c.fuhao*= -1;c.c = '1';}
    else if(a.c == 'i' && b.c == 'j') {c.c='k';}
    else if(a.c == 'i' && b.c == 'k') {c.fuhao*= -1;c.c = 'j';}

    else if(a.c == 'j' && b.c == 'i') {c.fuhao*= -1;c.c = 'k';}
    else if(a.c == 'j' && b.c == 'j') {c.fuhao*= -1;c.c = '1';}
    else if(a.c == 'j' && b.c == 'k') {c.c = 'i';}

    else if(a.c == 'k' && b.c == 'i') {c.c = 'j';}
    else if(a.c == 'k' && b.c == 'j') {c.fuhao*= -1;c.c = 'i';}
    else if(a.c == 'k' && b.c == 'k') {c.fuhao*= -1;c.c = '1';}

    return c;

}
bool is_k[N];

int main(){
    //freopen("../in.txt","r",stdin);
    int tt;
    LL x,l;
    string str;
    string tmp;
    scanf("%d",&tt);
    for(int cas=1;cas<=tt;cas++){
        memset(is_k,0,sizeof(is_k));
        cin>>x>>l;
        cin>>tmp;
        str = "";
        for(int i=1;i<=l;i++){
            str.append(tmp);
        }
        LL size = str.size();
        int first_i = -1;
        Item c;c.fuhao=1;c.c='1';
        for(int i=0;i<size;i++){
            c = mul(c,Item(1,str[i]));
            if(c.c == 'i' && c.fuhao==1 && first_i==-1){
                first_i = i;
            }
            else if(c.c == 'k' && c.fuhao == 1){
                is_k[i] = 1;
            }
        }
        c.c = '1';c.fuhao = 1;
        int last_k = -1;
        for(int i=size-1;i>=1;i--){
            c = mul(Item(1,str[i]),c);
            if(c.c == 'k' && c.fuhao == 1 && is_k[i-1]){
                last_k = i;
                break;
            }
        }
        if(last_k > first_i && first_i!=-1){
            printf("Case #%d: YES\n",cas );    
        }
        else{
            printf("Case #%d: NO\n",cas);
        }
    }
    return 0;
}