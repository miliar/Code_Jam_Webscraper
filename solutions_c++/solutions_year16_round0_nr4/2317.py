#include <cstdio>
#include <string>
#include <iostream>
#include <stdlib.h>
using namespace std;

int T,K,C,S;
int counter=1;

int main(){
    cin >> T;
    while (counter<=T){
        cin >> K;
        cin >> C;
        cin >> S;
        cout<<"Case #"<<counter<<": ";
        for (int i=1;i<=K;i++){
            cout<<i<<" ";
        }
        cout<<endl;
        counter++;
    }
}

//SoliDeoGloria

