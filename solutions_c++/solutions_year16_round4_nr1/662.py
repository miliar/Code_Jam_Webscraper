#include<iostream>
#include<vector>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<cstdio>
#include<algorithm>

using namespace std;

int T;

int n;
int av[3];

string best[15][3];

int counts[15][3][3];

int main() {
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);

    best[0][0]="R";
    best[0][1]="P";
    best[0][2]="S";

    counts[0][0][0]=1;
    counts[0][1][1]=1;
    counts[0][2][2]=1;

    for(int i=1;i<=12;i++) {
        for(int j=0;j<3;j++) {
            counts[i][0][j]=counts[i-1][0][j]+counts[i-1][2][j];
            counts[i][1][j]=counts[i-1][1][j]+counts[i-1][0][j];
            counts[i][2][j]=counts[i-1][1][j]+counts[i-1][2][j];
        }
        best[i][0]=min(best[i-1][0],best[i-1][2])+max(best[i-1][0],best[i-1][2]);
        best[i][1]=min(best[i-1][1],best[i-1][0])+max(best[i-1][1],best[i-1][0]);
        best[i][2]=min(best[i-1][1],best[i-1][2])+max(best[i-1][1],best[i-1][2]);
    }

    cin>>T;
    for(int C=0;C<T;C++) {
        cin>>n;
        for(int i=0;i<3;i++) cin>>av[i];
        bool any=false;
        string tb;
        for(int i=0;i<3;i++) {
            bool possible=true;
            for(int j=0;j<3;j++) {
                if(counts[n][i][j]!=av[j]) possible=false;
            }
            if(possible) {
                if(any) {
                    tb=min(tb,best[n][i]);
                } else {
                    any=true;
                    tb=best[n][i];
                }
            }
        }
        cout<<"Case #"<<C+1<<": ";
        if(any) {
                cout<<tb<<endl;
        } else {
            cout<<"IMPOSSIBLE"<<endl;
        }

    }
}
