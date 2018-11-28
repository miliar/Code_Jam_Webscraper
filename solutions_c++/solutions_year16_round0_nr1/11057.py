#include <bits/stdc++.h>
#include <iostream>
#include <cmath>
#include <string>
#include <algorithm>

// defines
#define modulo 1000000007
#define pi 3.1415926535897932384

typedef long long int lln;

using namespace std;

/*******************************************/
/*
        ya mas2la zebala accept b2a wenaby
                         O_O
                     ____________
                    /            \
                   /              \
                  /  /\       /\   \
         O_O     /   \/   |   \/    \     O_O
                 \        |_        /
                  \    \______/    /
                   \              /
                    \____________/

                         O_O

                    Khaled Ashraf
*/
lln check(lln X){
    bool arr[10]={};
    lln Z,mod,rkm;
    for(int i=1;;i++){
        Z=X*i;
        rkm=Z;
        while(Z){
            mod=Z%10;
            Z/=10;
            arr[mod]=1;
        }
        if(arr[0]==1 && arr[1]==1 && arr[2]==1 && arr[3]==1 && arr[4]==1 && arr[5]==1 && arr[6]==1 && arr[7]==1 && arr[8]==1 && arr[9]==1){
            return rkm;
        }
    }



}


int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("khaled.out", "w", stdout);

    lln T;
    cin>>T;
    for(int i=1;i<=T;i++){
        lln N;
        cin>>N;
        if(N==0){
            cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
        }
        else{
            cout<<"Case #"<<i<<": "<<check(N)<<endl;
        }
    }

    return 0;
}
