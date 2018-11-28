#include<iostream>
#include<cmath>
#include<cstring>
#include<cstdio>
#include<vector>
using namespace std;
int main(){
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int cases,i,j,n,m,t,k;
    bool fil,col,res;
    cin>>t;
    for(cases=1;cases<=t;cases++){
        cout<<"Case #"<<cases<<": ";
        cin>>n>>m;
        int a[n][m];
        for(i=0;i<n;i++){
            for(j=0;j<m;j++){
                cin>>a[i][j];
                }
            }
        res=true;
        for(i=0;i<n;i++){
            for(j=0;j<m;j++){
                fil=col=true;
                for(k=0;k<m;k++){
                    if(a[i][k]>a[i][j])fil=false;
                    }
                for(k=0;k<n;k++){
                    if(a[k][j]>a[i][j])col=false;
                    }
                if(!fil&&!col){
                    res=false;
                    }
                }
            }
        if(res)cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
        }
    }
