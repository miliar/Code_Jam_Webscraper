#include<iostream>
using namespace std;

int main(){
int t;
int i,j;
int n,m;
cin>>t;
int a[110][110];
for (int k=1; k<=t; k++)
    {
        int flag = 0;
        int flag1 = 0;
        cin>>n>>m;
        for (i=0; i<n; i++){
            for (j=0; j<m; j++){
                cin>>a[i][j];
            }
        }
        for (i=0; i<n && (flag ==0 || flag1 == 0); i++){
            for (j=0; j<m && (flag == 0 || flag1 == 0); j++){
                    for (int l=0; l<m ; l++){
                        if (a[i][j]<a[i][l]){
                            flag = 1;
                            //cout<<"i ="<<i<<"j = "<<j<<endl;
                          //  cout << "ll = " << l << endl;
                            break;
                        }
                        else {
                            flag = 0;
                        }
                    }
                    for (int q =0; q<n && flag == 1; q++){
                        if (a[i][j]<a[q][j]){
                            flag1 = 1;
                            // cout<<"i ="<<i<<"j = "<<j<<endl;
                            //cout <<"dd = " << q << endl;
                            break;
                        }
                        else {
                            flag1 = 0;
                        }
                    }
            }
        }
       // cout << "i = " << i << " " << "j = " << j << endl;
        if (flag ==1 && flag1 == 1){
            cout<<"Case #"<<k<<": "<<"NO"<<endl;
        }
        else {
            cout<<"Case #"<<k<<": "<<"YES"<<endl;
        }
    }
}
