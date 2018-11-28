#include<fstream>
//#include<iostream>
#include<cmath>

using namespace std;

int main(){
    int t;
    int x,r,c;
    ifstream cin("D-small-7.in");
    ofstream cout("D-small-7.out");
    cin>>t;
    for(int e=0;e<t;e++){
        cin>>x>>r>>c;
        bool can=1;

        if(x==1){
            can=1;
        }
        else if(x==2){
            if((r*c) % x ==0)can=1;
            else can=0;
        }
        else if(x==3){
            bool can2=1;
            can=1;
            if((r*c) % x !=0)can2=0;
            if(r==1 || c==1)can=0;
            can=can&&can2;
        }
        else if(x==4){
        bool can2=0;
            if((r*c) % x ==0)can2=1;

            if((r==4 && (c==3 || c==4))||(c==4 && (r==3 || r==4)))can =1;
            else can=0;
            can=can&&can2;
        }

        if(can)
        cout<<"Case #"<<e+1<<": "<<"GABRIEL"<<'\n';
        else
        cout<<"Case #"<<e+1<<": "<<"RICHARD"<<'\n';
    }
    cin.close();
    cout.close();
    return 0;
}
