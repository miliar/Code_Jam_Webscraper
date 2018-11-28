#include<iostream>
#include<vector>

using namespace std;

int main(){
    int x;
    cin>>x;
    for(int cases=0; cases<x; cases++){
        int a,b;
        cin>>a;
        int temp;
        vector<bool> data(17,0);
        for(int i=1; i<=4; i++){
            for(int j=0; j<4; j++){
                cin>>temp;
                if(i==a){
                    data[temp]=1;
                }
            }
        }
        int cnt=0;
        int res;
        cin>>b;
        for(int i=1; i<=4; i++){
            for(int j=0; j<4; j++){
                cin>>temp;
                if(i==b){
                    if(data[temp]==1){cnt++; res=temp;}
                }
            }
        }
        cout<<"Case #"<<cases+1<<": ";
        if(cnt==0){
            cout<<"Volunteer cheated!"<<endl;
          }else if(cnt==1){
            cout<<res<<endl;
        }else{cout<<"Bad magician!"<<endl;}
    }
    return 0;
}
