#include <iostream>
#include <cstdio>

using namespace std;

int ans[10];

int main(){
    freopen ("asmall.out","w",stdout);
    int t;
    cin>>t;
    for (int i=1;i<=t;i++){
        int n;
        cin>>n;
        int cas=0;
        int ca=0;
        for (int ii=1;ii<=4;ii++){
            for (int iii=1;iii<=4;iii++){
                int a;
                cin>>a;
                if (ii==n){
                    ans[iii]=a;
                }
            }
        }
        cin>>n;
        for (int ii=1;ii<=4;ii++){
            for (int iii=1;iii<=4;iii++){
                int a;
                cin>>a;
                if (ii==n){
                    for (int iiii=1;iiii<=4;iiii++){
                        if (ans[iiii]==a){
                            cas++;
                            ca=a;
                        }
                    }
                }
            }
        }
        cout <<"Case #"<<i<<": ";
        if (cas==0){
            cout <<"Volunteer cheated!"<<endl;
        }
        if (cas==1){
            cout <<ca<<endl;
        }
        if (cas>1){
            cout <<"Bad magician!"<<endl;
        }
    }
}
