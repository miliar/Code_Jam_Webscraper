#include<stdio.h>
#include<queue>
#include<string>
#include<string.h>
#include<algorithm>
#include<iostream>
using namespace std;

/*
0:0
1:1
2:i
3:j
4:k
*/
const int MAXN = 10010;
int go[5][5]={
    {0,0,0,0,0},
    {0,1,2,3,4},
    {0,2,-1,4,-3},
    {0,3,-4,-1,2},
    {0,4,3,-2,-1}
};
int a[MAXN],L,X;
int b[MAXN][MAXN];
void init(){
    char s[MAXN];
    scanf("%d%d",&L,&X);

    scanf("%s",s);
    string t(s),str="";
    for(int i=0; i<X; ++i)
        str+=t;
    //cout<<str<<endl;
    L = L*X;
    for(int i=0; i<L; ++i){
        if(str[i]=='i')
            a[i+1] = 2;
        else if(str[i]=='j')
            a[i+1] = 3;
        else if(str[i]=='k')
            a[i+1] = 4;
        else
            a[i+1] = 1;
    }
}
bool solve(){
    for(int i=1; i<=L; ++i){
        b[i][i] = a[i];
        for(int j=i+1; j<=L; ++j){
            int x = b[i][j-1];
            if(x<0) x=-x;
            b[i][j] = go[ x ][ a[j] ];
            if(b[i][j-1]<0) b[i][j]=-b[i][j];
        }
    }
    //[1,i]
    //[i+1,j]
    //[j+1,L]
    for(int i=1; i<=L-2; i++){
        if(b[1][i]!=2) continue;
        for(int j=i+1; j<=L-1; ++j)
            if(b[i+1][j]==3&&b[j+1][L]==4) return true;
    }
    return false;
}
int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int T,ca=1;
    scanf("%d",&T);
    while(T--){
        init();
        if(solve())
            printf("Case #%d: YES\n",ca++);
        else
            printf("Case #%d: NO\n",ca++);
    }
    return 0;
}
