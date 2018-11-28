#include<iostream>
#include<string>
using namespace std;
string vhod;
int main(){
    long long tests,t;
    cin>>tests;
    for(t=1;t<=tests;t++){
        cin>>vhod;
        string izhod;
        long long dulzina=vhod.size(),i;
        izhod+=vhod[0];
        for(i=1;i<dulzina;i++){
            if(vhod[i]>=izhod[0])
                izhod=vhod[i]+izhod;
            else
                izhod+=vhod[i];
        }
        cout<<"Case #"<<t<<": "<<izhod;
    }
    return 0;
}
