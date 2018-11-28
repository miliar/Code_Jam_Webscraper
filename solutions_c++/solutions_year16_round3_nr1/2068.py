//
//  main.cpp
//  googlekaz
//
//  Created by Dziugas Simaitis on 08/05/16.
//  Copyright © 2016 Dziugas Simaitis. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <queue>

using namespace std;

struct ball{
    char name;
    int kiekis;
};
bool operator<(ball const& x, ball const& y) {
    return x.kiekis < y.kiekis;
}
int main() {
    ifstream fin("A-large.in");
    ofstream cout("rez");
    int n;
    fin>>n;
    
    for(int q=0; q<n; q++){
        
        priority_queue<ball> eile;
        
        ball keitinys;
        int x, bendras_kiekis=0;
        fin>>x;
        for(int i=0; i<x; i++){
            fin>>keitinys.kiekis;
            keitinys.name='A'+i;
            bendras_kiekis+=keitinys.kiekis;
            eile.push(keitinys);
        }
        
        cout<<"Case #"<<q+1<<": ";
        while(bendras_kiekis>2){
            keitinys=eile.top();
            eile.pop();
            cout<<keitinys.name;
            keitinys.kiekis--;
            bendras_kiekis--;
            if(keitinys.kiekis!=0)
                eile.push(keitinys);
            if(bendras_kiekis>2){
            keitinys=eile.top();
            eile.pop();
            cout<<keitinys.name;
            keitinys.kiekis--;
            bendras_kiekis--;
            if(keitinys.kiekis!=0)
                eile.push(keitinys);
            }
            cout<<' ';
        }
        keitinys=eile.top();
        eile.pop();
        cout<<keitinys.name;
        keitinys.kiekis--;
        bendras_kiekis--;
            eile.push(keitinys);
        
            keitinys=eile.top();
            eile.pop();
            cout<<keitinys.name;
            keitinys.kiekis--;
            bendras_kiekis--;
            if(keitinys.kiekis!=0)
                eile.push(keitinys);
        
        cout<<endl;
    }
    return 0;
}
