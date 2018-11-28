#include <iostream>
#include <stdio.h>
#include <math.h>
#include <cstdlib>

#define REP(i, a, b)\
    for(int i = (int)a; i<=(int)b; i++)

using namespace std;

int main(){
    int t;
    cin>>t;
    int count = 0;

    while(t--){
        int x, r, c;
        cin>>x>>r>>c;
        count++;

        if(x==1){
            cout<<"Case #"<<count<<": "<<"GABRIEL"<<endl;
        }
        else if (x == 2 ){
            if((r*c)%2==0){
                cout<<"Case #"<<count<<": "<<"GABRIEL"<<endl;
            }
            else{
                cout<<"Case #"<<count<<": "<<"RICHARD"<<endl;
            }
        }
        else if(x == 3){

            if((r*c)%3==0&& r!=1 && c!=1){
                cout<<"Case #"<<count<<": "<<"GABRIEL"<<endl;
            }
            else{
                cout<<"Case #"<<count<<": "<<"RICHARD"<<endl;
            }
        }
        else if(x == 4){
            if((r*c)%4 == 0 && r !=2 && c!=2 && r!=1 && c!=1)
                cout<<"Case #"<<count<<": "<<"GABRIEL"<<endl;
            else{
                cout<<"Case #"<<count<<": "<<"RICHARD"<<endl;
            }
        }

    }
    return 0;
}

