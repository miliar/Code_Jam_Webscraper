#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;


int analytic(int tot,string Str){
    int added = 0;
    int Aadded = 0;

    Aadded+=Str[0]-'0';

    for(int i=0;i<tot;i++){
        if(i+1>Aadded){
            added+=1;
            Aadded+=1;
        };
        Aadded+=Str[i+1]-'0';
    }
    return added;

}



int main()
{
    int T=0,Lt=0;
    string StrA;
    cin>>T;
    for(int i=0;i<T;i++){
        cin>>Lt;
        cin>>StrA;
        cout<<"Case #"<<i+1<<": "<<analytic(Lt,StrA)<<endl;
    }
}
