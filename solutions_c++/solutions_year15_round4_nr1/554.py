#include<iostream>
#include<vector>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<cstdio>


using namespace std;

int t;
int r,c;

int ans;

char g[200][200];

bool isOk(int y, int x) {
    if(g[y][x]=='^') {
        for(int i=y-1;i>=0;i--) {
            if(g[i][x]!='.') return true;
        }
        return false;
    }
    if(g[y][x]=='v') {
        for(int i=y+1;i<r;i++) {
            if(g[i][x]!='.') return true;
        }
        return false;
    }
    if(g[y][x]=='>') {
        for(int j=x+1;j<c;j++) {
            if(g[y][j]!='.') return true;
        }
        return false;
    }
    if(g[y][x]=='<') {
        for(int j=x-1;j>=0;j--) {
            if(g[y][j]!='.') return true;
        }
        return false;
    }
}

int main() {
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);

    cin>>t;
    for(int cases=0;cases<t;cases++) {
        cin>>r>>c;
        for(int i=0;i<r;i++) {
            cin>>g[i];
        }
        bool imp=false;
        int ans=0;
        for(int i=0;i<r;i++) {
            for(int j=0;j<c;j++) {
                if(g[i][j]!='.') {
                    if(!isOk(i,j)) {
                        ans++;
                        bool anyok=false;
                        g[i][j]='^';
                        if(isOk(i,j)) anyok=true;
                        g[i][j]='>';
                        if(isOk(i,j)) anyok=true;
                        g[i][j]='<';
                        if(isOk(i,j)) anyok=true;
                        g[i][j]='v';
                        if(isOk(i,j)) anyok=true;
                        if(!anyok) imp=true;
                    }
                }
            }
        }
        if(imp) {
            cout<<"Case #"<<cases+1<<": "<<"IMPOSSIBLE"<<endl;
        } else {
            cout<<"Case #"<<cases+1<<": "<<ans<<endl;
        }
    }
}
