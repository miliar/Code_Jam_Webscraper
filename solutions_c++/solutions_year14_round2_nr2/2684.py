#include<iostream>


using namespace std;

int main(){
    int t,a,b,k,chances=0,T=0;
    cin>>t;
    while(t--!=0){
        T++;
        cin>>a>>b>>k;
        for(int i=0;i<a;i++){
            for(int j=0;j<b;j++)
                if((i&j)<k)  {//cout<<i<<'\t'<<b<<endl;
                        chances++;}
        }
        cout<<"Case #"<<T<<": "<<chances<<endl;
        chances=0;
    }
    return 0;
}


