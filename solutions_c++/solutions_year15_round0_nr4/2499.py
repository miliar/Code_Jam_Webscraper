#include<iostream>
#include<cstdio>
using namespace std;

void asd(){
    int x,r,c;
    cin >> x >> r >> c;
    if(x==1){cout << "GABRIEL\n";}
    if(x==2){
             if(r*c%2==0){
                          cout << "GABRIEL\n";
             }else{cout << "RICHARD\n";}
    }
    if(x==3){
             if(r*c%3==0 and max(r,c)>=3 and min(r,c)>=2){
                         cout << "GABRIEL\n";
             }else{cout << "RICHARD\n";}
    }
    if(x==4){
             if(r*c%4==0 and max(r,c)>=4 and min(r,c)>=3){
                         cout << "GABRIEL\n";
             }else{cout << "RICHARD\n";}
    }
}           

int main(){
    freopen ("D-small-attempt1.in","r",stdin);
    freopen ("D-small-attempt1.out","w",stdout);
    int t;
    cin >> t;
    for(int i=1; i<=t; i++){
            cout << "Case #" << i << ": ";
            asd();
    }
    return 0;
}
