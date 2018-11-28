/* 
 * File:   main.cpp
 * Author: Proprietario
 *
 * Created on 12 aprile 2014, 20.09
 */

#include <cstdlib>
#include <fstream>
#include <iostream>
#include <iomanip> 
using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    ifstream in("B-large.in");
    ofstream out("output.out");
    int T;
    in>>T;
    double  C, F, X, N;
    
    for(int i=0; i<T; i++){
        bool sent=true;
        in>>C>>F>>X;
        //cout<<C<<" "<<F<<" "<<X<< " ";
        N=2.0000000;
        double costo=0, time=costo+X/N, time1;
        N+=F;
        //cout<<"N="<<N<<" ";
        do{
            costo=costo+(C/(N-F));
            time1=costo+X/N;
            N+=F;
            //cout<<time1<< " ";
            if(time>time1){
                time=time1;
            }
            else{
                if(time<time1){
                    sent=false;
                }
            }
        }while(sent);
        //cout<<endl;
        out<<"Case #"<<i+1<<": "<<setprecision(10)<<time<<endl;
    }
    return 0;
}

