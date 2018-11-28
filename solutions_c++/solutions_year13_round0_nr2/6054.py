#include<iostream>
#define sz 110
#include<stdio.h>
#include<cstring>

using namespace std;

int lawn[sz][sz],rmax[sz],cmax[sz];

bool code(int n,int m){
    for(int i=1; i<=n; i++){
        for(int j=1; j<=m; j++){
            if(lawn[i][j]-rmax[i]<0 && lawn[i][j]-cmax[j]<0){
                return false;
            }
        }
    }
    return true;
}

int main(){
    freopen("Bsmalloutput.txt","w",stdout);
    int T,cases = 1;
    cin>>T;
    while(T--){
        memset(rmax,0,sizeof(rmax));
        memset(cmax,0,sizeof(cmax));
        int n,m;
        cin>>n>>m;
        for(int i=1; i<=n; i++){
            for(int j=1; j<=m; j++){
                cin>>lawn[i][j];
                if(lawn[i][j]>rmax[i]) rmax[i] = lawn[i][j];
                if(lawn[i][j]>cmax[j]) cmax[j] = lawn[i][j];
            }
        }
        if(code(n,m)) cout<<"Case #"<<cases++<<": YES"<<endl;
        else cout<<"Case #"<<cases++<<": NO"<<endl;
    }
    return 0;
}
