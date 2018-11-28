#include<iostream>
using namespace std;

int main(){
    int T;
    cin>>T;
    int A[4][4],B[4][4];
    for(int p=1;p<=T;p++){
        int a,b;
        cin>>a;
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                cin>>A[i][j];
            }
        }
        cin>>b;
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                cin>>B[i][j];
            }
        }
        int sum=0,ans=0;
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                if(A[a-1][i]==B[b-1][j]){
                    sum++;
                    ans=A[a-1][i];
                }
            }
        }
        if(sum==1) cout<<"Case #"<<p<<": "<<ans<<endl;
        else if(sum==0) cout<<"Case #"<<p<<": Volunteer cheated!\n";
        else cout<<"Case #"<<p<<": Bad magician!\n";
    }
    return 0;
}
