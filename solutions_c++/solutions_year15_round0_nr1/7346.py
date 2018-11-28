#include<iostream>
#include<sstream>
#include<string>
#include<cstdio>
using namespace std;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,sMax,s[1010],total,required,totalReq,j=0;
    cin>>t;
    while(t--){
        total=0,totalReq=0;
        cin>>sMax;
        for(int i=0;i<sMax+1;i++){
            scanf("%1d",&s[i]);
        }
        total+=s[0];
        for(int i=1;i<sMax+1;i++){
            if(s[i]!=0){
                if(total>=i){
                    total+=s[i];
                }
                else{
                    required=i-total;
                    totalReq+=required;
                    total=total+required+s[i];
                    required=0;
                }
            }
        }
        cout<<"Case #"<<++j<<": "<<totalReq<<endl;

    }
}
