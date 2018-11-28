#include <iostream>
#include <cstdio>
#include <map>
using namespace std;

main(){
    freopen("D-small-attempt2.in", "r", stdin);
    freopen("Doutput1.txt", "w", stdout);
    int t = 0;
    int x,r,c;
    string nombre;
    cin>>t;
    for(int tc=1;tc<=t;tc++){
        cin>>x>>r>>c;
        nombre = "";
        if(x==1){
            nombre="GABRIEL";
        }else if(x==2){
            if(r*c%2==0){
                nombre="GABRIEL";
            }else{
                nombre="RICHARD";
            }
        }else if(x==3){
            if(r*c%3==0 && r*c>=6){
                nombre="GABRIEL";
            }else{
                nombre="RICHARD";
            }
        }else if(x==4){
            if(r*c>=12){
                nombre="GABRIEL";
            }else{
                nombre="RICHARD";
            }
        }
        cout<<"Case #"<<tc<<": "<<nombre<<endl;
    }
}
