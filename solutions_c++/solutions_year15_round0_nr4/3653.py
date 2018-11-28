#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

int main(void)
{
    string cadena;
    ifstream in;
    ofstream out;
    int cas,t;
    int X,R,C;

    in.open("D-small-attempt5.in",ios::in);
    out.open("Output.in",ios::out);

    getline(in,cadena,'\n');
    t=atoi(cadena.c_str());

    for(cas=0;cas<t;cas++){
        getline(in,cadena,' ');
        X=atoi(cadena.c_str());
        getline(in,cadena,' ');
        R=atoi(cadena.c_str());
        getline(in,cadena,'\n');
        C=atoi(cadena.c_str());

        cout<<X<<" "<<R<<" "<<C<<endl;
        if(R==1&&C==1&&X==1){
            cout<<"Case #"<<cas+1<<": GABRIEL"<<endl;
            out<<"Case #"<<cas+1<<": GABRIEL"<<endl;
        }else if(R==2&&C==1&&X==2){
            cout<<"Case #"<<cas+1<<": GABRIEL"<<endl;
            out<<"Case #"<<cas+1<<": GABRIEL"<<endl;
        }else if(C==2&&R==1&&X==2){
            cout<<"Case #"<<cas+1<<": GABRIEL"<<endl;
            out<<"Case #"<<cas+1<<": GABRIEL"<<endl;
        }else{
            if((R*C)%X==0&&(R*C)>X){
                if(R>(X/2)&&C>(X/2)){
                    cout<<"Case #"<<cas+1<<": GABRIEL"<<endl;
                    out<<"Case #"<<cas+1<<": GABRIEL"<<endl;
                }else if((R>=X*2&&R%X==0)||(C>=X*2&&C%X==0)){
                    cout<<"Case #"<<cas+1<<": GABRIEL"<<endl;
                    out<<"Case #"<<cas+1<<": GABRIEL"<<endl;
                }else{
                    cout<<"Case #"<<cas+1<<": RICHARD"<<endl;
                    out<<"Case #"<<cas+1<<": RICHARD"<<endl;
                }
            }else{
                cout<<"Case #"<<cas+1<<": RICHARD"<<endl;
                out<<"Case #"<<cas+1<<": RICHARD"<<endl;
            }
        }
        cout<<endl;
    }

    in.close();
    out.close();
    return 0;
}
