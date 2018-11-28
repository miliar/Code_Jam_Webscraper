#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T,caseNum=1;
    cin >> T;
    while(T--){
        string x;
        cin>>x;
        int i = 0,counter=0 ;

        while(i<x.length() - 1){
            if(x[i]!=x[i+1])
                counter++;

            i++;
        }

    if(x[x.length()-1]=='-')
        counter++;

    cout<<"Case #"<<caseNum++<<": "<<counter<<endl;
    }
}
