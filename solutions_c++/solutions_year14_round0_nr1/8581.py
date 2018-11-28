#include <iostream>
using namespace std;

int main() {
    int t;
    cin>>t;
    for(int i=0;i<t;i++){
        int c1,c2,j,k,pos,match=0;
        int a1[4][4],a2[4][4];
        cin>>c1;
        for(j=0;j<4;j++){
            for(k=0;k<4;k++){
                cin>>a1[j][k];
            }
        }
        cin>>c2;
        for(j=0;j<4;j++){
            for(k=0;k<4;k++){
                cin>>a2[j][k];
            }
        }
        for(j=0;j<4;j++){
            for(k=0;k<4;k++){
                if(a1[c1-1][j]==a2[c2-1][k]){
                    pos=j;
                    match++;
                }
            }
        }
        if(match>1){
            cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
            continue;
        }
        if(match==1){
            cout<<"Case #"<<i+1<<": "<<a1[c1-1][pos]<<endl;
            continue;
        }
        if(match==0){
            cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
                    continue;
        }
    }
        return 0;
}
