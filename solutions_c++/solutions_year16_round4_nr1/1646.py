#include<bits/stdc++.h>
#define f first
#define s second
#define mp make_pair
#define pb push_back
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
char odp[100];
bool kon=false;
char walcz(char a,char b){
    if(a>b)swap(a,b);
    if(a==b)return 'N';
    if(a=='P' && b=='R')return 'P';
    if(a=='P' && b=='S')return 'S';
    if(a=='R' && b=='S')return 'R';
}
void check(int siz){
    for(int i=siz-1;i>0;i--){
        odp[i]=walcz(odp[2*i],odp[2*i+1]);
        if(odp[i]=='N')return;
    }
    kon=true;
    for(int i=0;i<siz;i++)
        printf("%c",odp[i+siz]);
    puts("");
}
void gen(int x,int siz,int p,int r,int s){
    if(x==siz)check(siz);
    if(kon)return;
    if(p>0){
        odp[siz+x]='P';
        gen(x+1,siz,p-1,r,s);
    }
    if(kon)return;
    if(r>0){
        odp[siz+x]='R';
        gen(x+1,siz,p,r-1,s);
    }
    if(kon)return;
    if(s>0){
        odp[siz+x]='S';
        gen(x+1,siz,p,r,s-1);
    }
}
int main(){
    int t; scanf("%d",&t);
    for(int test=1;test<=t;test++){
        int n,p,r,s; scanf("%d%d%d%d",&n,&r,&p,&s);
        kon=false;
        printf("Case #%d: ",test);
        gen(0,(1<<n),p,r,s);
        if(!kon)puts("IMPOSSIBLE");
    }
    return 0;
}

