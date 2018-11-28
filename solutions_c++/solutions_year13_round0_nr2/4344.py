#include<cstdio>
#include<iostream>
#include<cmath>
#include<algorithm>
#include<cstdlib>
using namespace std;
const int nmax=111;
#define FOR(i,a,b) for (int (i)=a;i<=b;i++)
#define DFOR(i,a,b) for (int (i)=a;i>=b;i--)
int test;
int n,m;
int a[nmax][nmax];
int m_h;
int b[nmax][nmax];
int r[nmax];
int c[nmax];
int read(){
    cin>>n>>m;
    m_h=1;
    FOR(i,1,n) FOR(j,1,m) {
        cin>>a[i][j];
        if (a[i][j]>m_h) m_h=a[i][j];
    }
    return 0;
}
bool solution(){
    FOR(h,1,100){
        FOR(i,1,n) r[i]=0;
        FOR(j,1,m) c[j]=0;
        FOR(i,1,n) FOR(j,1,m) if (a[i][j]<=h) b[i][j]=1; else b[i][j]=0;
        FOR(i,1,n) FOR(j,1,m) if (b[i][j]==1) {r[i]++; c[j]++;}
        FOR(i,1,n) if (r[i]==m) FOR(j,1,m) b[i][j]=-1;
        FOR(j,1,m) if (c[j]==n) FOR(i,1,n) b[i][j]=-1;
        FOR(i,1,n) FOR(j,1,m) if (b[i][j]==1) return false;
    }
    return true;
}
int main(){
    freopen("lawn.txt","w",stdout);
   cin>>test;
   FOR(t,1,test){
        read();
        cout<<"Case #"<<t<<": ";
        if (solution()) cout<<"YES"; else cout<<"NO";
        cout<<endl;
    }
    return 0;
}
/*
3
3 3
2 1 2
1 1 1
2 1 2
5 5
2 2 2 2 2
2 1 1 1 2
2 1 2 1 2
2 1 1 1 2
2 2 2 2 2
1 3
1 2 1
*/
