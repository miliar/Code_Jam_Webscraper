#include <bits/stdc++.h>
#define F first
#define S second
using namespace std;
typedef long long ll;

string m[111];

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int tcs;
    cin>>tcs;
    for (int tc=1;tc<=tcs;tc++){
        cout<<"Case #"<<tc<<": ";
        int r,c;
        cin>>r>>c;
        for (int i=0;i<r;i++){
            cin>>m[i];
        }
        int vv=0;
        for (int i=0;i<r;i++){
            for (int ii=0;ii<c;ii++){
                int a=0;
                int y=0;
                int v=0;
                int o=0;
                for (int j=ii+1;j<c;j++){
                    if (m[i][j]!='.'){
                        o=1;
                        break;
                    }
                }
                for (int j=ii-1;j>=0;j--){
                    if (m[i][j]!='.'){
                        v=1;
                        break;
                    }
                }
                for (int j=i+1;j<r;j++){
                    if (m[j][ii]!='.'){
                        a=1;
                        break;
                    }
                }
                for (int j=i-1;j>=0;j--){
                    if (m[j][ii]!='.'){
                        y=1;
                        break;
                    }
                }
                if (m[i][ii]=='>'&&o==0){
                    if (a+y+o+v==0){
                        vv=-1;
                        goto loppu;
                    }
                    vv++;
                }
                if (m[i][ii]=='<'&&v==0){
                    if (a+y+o+v==0){
                        vv=-1;
                        goto loppu;
                    }
                    vv++;
                }
                if (m[i][ii]=='^'&&y==0){
                    if (a+y+o+v==0){
                        vv=-1;
                        goto loppu;
                    }
                    vv++;
                }
                if (m[i][ii]=='v'&&a==0){
                    if (a+y+o+v==0){
                        vv=-1;
                        goto loppu;
                    }
                    vv++;
                }
            }
        }
        loppu:;
        if (vv==-1){
            cout<<"IMPOSSIBLE"<<endl;
        }
        else{
            cout<<vv<<endl;
        }
    }
}
