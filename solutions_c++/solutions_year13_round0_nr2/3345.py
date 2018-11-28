#include<iostream>
#include<cstdlib>
#include<cstring>
#include<cmath>
using namespace std;

int main(){
    int t,f,a[110][110];
    cin>>t;
    for (int tt=1; tt<t+1; ++tt){
        f=1;
        int n,m; cin>>n>>m;
        int red[110],stup[110];
        memset(red, 0, sizeof(red));
        memset(stup, 0, sizeof(stup));
        for (int i=0; i<n; ++i){
            for (int j=0; j<m; ++j){
                cin>>a[i][j];
                //cout<<endl<<"B"<<i<<" "<<j<<" "<<a[i][j]<<" "<<red[i]<<" "<<stup[j]<<endl;
                red[i]=max(red[i],a[i][j]);
                stup[j]=max(stup[j], a[i][j]);
            }
        }
         for (int i=0; i<n&&f; ++i){
            for (int j=0; j<m&&f; ++j){
                if (a[i][j]<red[i]&&a[i][j]<stup[j]){ f=0; /*cout<<endl<<"A"<<i<<" "<<j<<" "<<red[i]<<" "<<red[j]<<endl;*/}
            }
        }


        cout<<"Case #"<<tt<<": ";
        if (f) cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
    }
    return 0;
}
