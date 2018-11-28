#include <iostream>
#include <stdio.h>
#include <conio.h>
#include <math.h>
#include <string>

using namespace std;

int main(){
    int t, tt, x, r, c;
    bool sw;
    cin>>t;
    tt=0;
    while(tt++ < t){
        cin>>x>>r>>c;
        sw = false;
        if((r*c)%x==0 && r>=(x-1) && c>=(x-1) && (x%2==1||(r*c)%2==0))
            sw = true;

        cout<<"Case #"<<tt<<": "<<(sw?"GABRIEL":"RICHARD")<<endl;
    }
    return 0;
}