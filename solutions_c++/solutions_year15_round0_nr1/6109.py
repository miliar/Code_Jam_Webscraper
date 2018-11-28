#include<iostream>
using namespace std;


int main(){
    int t,sm,res,tot;
    string shy;
    cin>>t;
    for(int w=1;w<=t;w++){
        cin>>sm>>shy;
        res=0,tot=0;
        for(int i=0;i<=sm;i++){
            if(tot<i){
                res+=(i-tot);
                tot=i;
            }
            tot+=(shy[i]-'0');

        }

        cout<<"Case #"<<w<<": "<<res<<endl;
    }
}
