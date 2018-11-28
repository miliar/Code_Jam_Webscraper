
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <stdlib.h>
#include <stdio.h>
#include <string>

using namespace std;

int main(){

    int T,smax,digits[1002],digstr,temp, cumsum=0, invites,j=1;
    freopen ("A-small-attempt1.in","r",stdin);
    freopen ("out.out","w",stdout);

    cin>>T;
    while(j<=T){
        cumsum=0;
        invites=0;
        cin>>smax;
        cin>>digstr;
        for(int i=smax;i>=0;i--){
            temp=digstr%10;
            digits[i]=temp;
            digstr/=10;
        }
        for(int i=0;i<=smax;i++){
            if(cumsum<i && digits[i]>0){
                invites+=i-cumsum;
                cumsum+=invites;
            }
            cumsum+=digits[i];
        }
        cout<<"Case #"<<j<<": "<<invites<<endl;
        j++;
    }
    return 0;
}
