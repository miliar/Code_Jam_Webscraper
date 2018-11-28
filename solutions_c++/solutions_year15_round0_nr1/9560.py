#include <iostream>
using namespace std;
int main(){
    int t;
    cin>>t;
    for(int tcase=1;tcase<=t;++tcase){
        int smax;
        cin>>smax;
        string str;
        cin>>str;
        cout<<"Case #"<<tcase<<": ";
        if(smax==0){
            cout<<0<<endl;
        }else{
            int num=0;
            int tot=0;
            int falta=0;
            for(int i=0;i<=smax;++i){
                if(tot<i){
                    falta+=i-tot;
                    tot=i;
                }
                tot+=str[i]-'0';
            }
            cout<<falta<<endl;
        }
    }
}