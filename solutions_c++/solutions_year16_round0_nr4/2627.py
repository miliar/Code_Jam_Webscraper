#include <bits/stdc++.h>
#include <fstream>
using namespace std;

int main(){
    fstream potato;
    ofstream optato;
    string meh;
    optato.open("Answer.txt");
    potato.open("D-small-attempt0.in");
    int tiems=0, temp=0, tmep=0, tpem=0;
    potato >> tiems;
    for(int i=0; i<tiems; i++){
        potato >> temp;
        potato >> tmep;
        potato >> tpem;
        optato << "Case #" << i+1 << ": ";
        for(int k=0; k<temp; k++){
            optato << k+1 << " ";
        }
        optato << "\n";
    }
optato.close();
}
