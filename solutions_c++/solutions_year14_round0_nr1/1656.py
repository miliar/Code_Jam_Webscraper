#include <iostream>
using namespace std;
int A[4][4];
int B[4][4];
int main(int argc, char *argv[]){
    int T;
    cin >> T;
    for(int c=1;c<=T;++c){
        int r0, r1;
        cin >> r0;
        --r0;
        for(int i=0;i<4;++i){
            for(int j=0;j<4;++j){
                cin >> A[i][j];
            }
        }
        cin >> r1;
        --r1;
        for(int i=0;i<4;++i){
            for(int j=0;j<4;++j){
                cin >> B[i][j];
            }
        }
        int cnt=0;
        int selected=-1;
        for(int j=0;j<4;++j){
            for(int k=0;k<4;++k){
                if( A[r0][j] == B[r1][k] ){
                    ++cnt;
                    selected = A[r0][j];
                }
            }
        }
        if(cnt==0){
            cout<<"Case #"<<c<<": "<<"Volunteer cheated!"<<endl;
        }else if(cnt==1){
            cout<<"Case #"<<c<<": "<<selected<<endl;
        }else{
            cout<<"Case #"<<c<<": "<<"Bad magician!"<<endl;
        }
    }

	return 0;
}
