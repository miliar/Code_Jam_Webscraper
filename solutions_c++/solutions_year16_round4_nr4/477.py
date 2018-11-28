#include<iostream>
#include<vector>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<cstdio>
#include<algorithm>
#include<iomanip>

using namespace std;

int T;

int n;
bool o[5][5];
int ans;
int tans;

bool taken[5];
bool filled[5];


bool g(int x) {
    if (x==0) return true;
    for(int i=0;i<n;i++) {
        if(!taken[i]) {
            taken[i]=true;
            bool anyfill=false;
            for(int j=0;j<n;j++) {
                if(o[i][j]&&!filled[j]) {
                    filled[j]=true;
                    anyfill=true;
                    if(!g(x-1)) {
                        return false;
                    }
                    filled[j]=false;
                }
            }
            if(!anyfill) return false;
            taken[i]=false;
        }
    }
    return true;
}


void brute(int x, int y) {
    if(y==n) {
            brute(x+1,0);
    } else {
        if(x!=n) {
            if(o[x][y]) {
                brute(x,y+1);
            } else {
                brute(x,y+1);
                tans++;
                o[x][y]=true;
                brute(x,y+1);
                o[x][y]=false;
                tans--;
            }
        } else {
            memset(taken,0,sizeof(taken));
            memset(filled,0,sizeof(filled));
            if(g(n)) {
                ans=min(ans,tans);
            }
        }
    }
}

int main() {
    freopen("d.in","r",stdin);
    freopen("d.out","w",stdout);


    cin>>T;
    for(int C=0;C<T;C++) {
        cin>>n;
        string s;
        memset(o,false,sizeof(o));
        for(int i=0;i<n;i++) {
            cin>>s;
            for(int j=0;j<n;j++) {
                if(s[j]=='1') o[i][j]=true;
            }
        }
        ans=200;
        tans=0;
        brute(0,0);
        cout<<"Case #"<<C+1<<": "<<setprecision(20)<<ans<<endl;

    }
}
