#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main(){
    int i,j,k,l,m,n,t,c=0,q;
    int a[4][4],b[4][4],z[4],x[4];
    cin>>t;
    while(t--){
        cin>>m;
        c++;
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                cin>>a[i][j];
            }
            if(i==m-1){
                for(j=0;j<4;j++){
                    z[j]=a[i][j];
                }
            }
        }
        cin>>n;
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                cin>>b[i][j];
            }
            if(i==n-1){
                    l=0,k=0;
                    for(q=0;q<4;q++){
                        for(j=0;j<4;j++){
                            if(z[q]==b[i][j]){
                                l++;
                                k=z[q];break;
                            }
                        }
                    }
            }
        }

        if(l==0){
          cout<<"Case #"<<c<<": Volunteer cheated!\n";
        }
        else if (l==1){
            cout<<"Case #"<<c<<": "<<k<<'\n';
        }
        else{
            cout<<"Case #"<<c<<": Bad magician!\n";
        }
    }
return 0;
}
