#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <cmath>
#include <iostream>
#include <fstream>

using namespace std;

typedef long long LL;
#define INF 1e9;
#define NINF -1*1e9;
#define mod 1e9+9;
#define fori(n) for (int i=1;i<=n;i++)
#define forj(n) for (int j=1;j<=n;j++)
#define fork(n) for (int k=1;k<=n;k++)
#define for2i(a,b) for (int i=a;i<=b;i++)
#define for2j(a,b) for (int j=a;j<=b;j++)
#define forii(a,b) for (int i=b;i>=a;i--)
#define forji(a,b) for (int j=b;j>=a;j--)
#define pi 3.14159265;

bool prime(int m){
    int u=sqrt(m);
    for2i(2,u+1){
        if (m%i==0){return false;}
    }
    return true;
}

LL max(LL a,LL b){if (a>b){return a;} else {return b;}}
LL min(LL a,LL b){if (a<b){return a;} else {return b;}}

void solve(int q){
    int ma[5][5];
    int empt=0;
    fori(4){forj(4){ma[i][j]=0;}}
    fori(4){
        string x;
        cin>>x;
        for2j(0,3){
            if (x[j]=='X'){ma[i][j+1]=1;}
            else if (x[j]=='O'){ma[i][j+1]=2;}
            else if (x[j]=='T'){ma[i][j+1]=3;}
            else {empt=1;}
        }

        }
    int st=0;
    fori(4){
        int st1=1,st2=1;

        forj(4){
            if ((ma[i][j]==2)||(ma[i][j]==0)){st1=0;}
            if ((ma[i][j]==1)||(ma[i][j]==0)){st2=0;}
        }
        if (st1==1){st=1;}
        if (st2==1){st=2;}
    }
    fori(4){
        int st1=1,st2=1;
        forj(4){
            if ((ma[j][i]==2)||(ma[j][i]==0)){st1=0;}
            if ((ma[j][i]==1)||(ma[j][i]==0)){st2=0;}
        }
        if (st1==1){st=1;}
        if (st2==1){st=2;}



    }

    int st1=1,st2=1;

        forj(4){
            if ((ma[j][j]==2)||(ma[j][j]==0)){st1=0;}
            if ((ma[j][j]==1)||(ma[j][j]==0)){st2=0;}
        }
        if (st1==1){st=1;}
        if (st2==1){st=2;}

    st1=1,st2=1;

        forj(4){
            if ((ma[j][5-j]==2)||(ma[j][5-j]==0)){st1=0;}
            if ((ma[j][5-j]==1)||(ma[j][5-j]==0)){st2=0;}
        }
        if (st1==1){st=1;}
        if (st2==1){st=2;}

    cout<<"Case #"<<q<<": ";
    if (st==1){cout<<"X won"<<endl;}
    else if (st==2){cout<<"O won"<<endl;}
    else if (st==0){
        if (empt==0){cout<<"Draw"<<endl;}
        else {cout<<"Game has not completed"<<endl;}


    }
}
bool file=true;
int main(){
    if (file){
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);
    }
    int N;
    scanf("%d",&N);
    fori(N){solve(i); }
    return 0;
}
