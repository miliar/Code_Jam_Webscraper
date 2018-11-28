#include <iostream>
#include <cstdio>
#include <map>
using namespace std;
string tm;
int s;
int main(){
    freopen("A-large.in", "r", stdin);
    freopen("Aoutputlargo.txt", "w", stdout);
    int t = 0;
    cin>>t;
    for(int tc=1;tc<=t;tc++){
        cin>>s>>tm;
        int cont = 0;
        int inv = 0;
        for(int i=0;i<tm.size();i++){
            if(tm[i]!='0'){
                //cout<<tm[i]-48;
                //cout<<i<<"::"<<cont<<endl;
                if(i>cont){
                    inv+=i-cont;
                    cont+=(i-cont);
                }
                cont+=tm[i]-'0';
            }
        }
        cout<<"Case #"<<tc<<": "<<inv<<endl;
    }
    return 0;
}
