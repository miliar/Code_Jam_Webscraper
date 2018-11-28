#include <iostream>
#include <cstring>
#include <cstdio>
#include <queue>

using namespace std;

long long i,j,k,l,m,n, v, cur , r,c,w,test,t, mx, a[105],d,dd ,ii,x;
string alphabet, s[105];

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w", stdout);
    cin>>t;

    while(t--){
        cin>>r>>c;
        test++;
        for (i=0;i<r;i++){
            cin>>s[i];
        }
        int ans = 0, imp = 0;
        for (i=0;i<r;i++){
            for (j=0;j<c;j++){
                if (s[i][j]!='.'){
                    int open1 = 1, open2 =1, open3 = 1, open4 = 1;
                    for (k=i-1;k>=0;k--){
                        if (s[k][j]!='.') {open1 = 0;break;}
                    }
                    for (k=i+1;k<r;k++){
                        if (s[k][j]!='.') {open2 = 0;break;}
                    }                    
                    for (k=j-1;k>=0;k--){
                        if (s[i][k]!='.') {open3 = 0;break;}
                    }
                    for (k=j+1;k<c;k++){
                        if (s[i][k]!='.') {open4 = 0;break;}
                    }
                    if (open1+open2+open3+open4==4){
                        imp = 1;
                    }
                    if (s[i][j]=='^') ans+=open1; else
                    if (s[i][j]=='v') ans+=open2; else
                    if (s[i][j]=='<') ans+=open3; else
                    if (s[i][j]=='>') ans+=open4;                                        
                }
            }
        }
        if (imp)
            cout<<"Case #"<<test<<": IMPOSSIBLE\n"; else
            cout<<"Case #"<<test<<": "<<ans<<"\n";
    } 
    return 0;
}
