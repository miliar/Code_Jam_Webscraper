#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;
int main(){
    int t,n,m,a[5][5],b[5][5],c,i,j,ans;
    cin>>t;
    for(int k = 1; k <= t; k++){
        cin>>n;
        for(i =0 ;i <4; i++){
            for(j = 0; j < 4; j++){
                cin>>a[i][j];
            }
        }
        cin>>m;
        for(i =0 ;i <4; i++){
            for(j = 0; j < 4; j++){
                cin>>b[i][j];
            }
        }
        c = 0;
        for(i =0 ;i <4; i++){
            for(j = 0; j < 4; j++){
                if(a[n - 1][i] == b[m -1][j]){
                    ans = a[n-1][i];
                    c++;
                }
            }
        }
        if(c == 0)
            cout<<"Case #"<<k<<": Volunteer cheated!"<<endl;
        else if(c == 1)
            cout<<"Case #"<<k<<": "<<ans<<endl;
        else
            cout<<"Case #"<<k<<": Bad magician!"<<endl;
    }
}
