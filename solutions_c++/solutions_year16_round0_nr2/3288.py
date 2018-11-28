#include <bits/stdc++.h>
#include <fstream>
using namespace std;

int main(){
    fstream potato;
    ofstream optato;
    string meh;
    optato.open("Answer.txt");
    potato.open("B-large.in");
    int tiems=0, countah=0, curarns=0;
    potato >> tiems;
    for(int i=0; i<tiems; i++){
            countah=0;
    curarns=0;
        potato >> meh;
        for(int k=0; k<meh.size(); k++){
            if((meh[meh.size()-k-1] == '+' && countah == 1)||(meh[meh.size()-k-1] == '-' && countah == 0)){
                countah = (countah+1)%2;
                curarns++;
            }
        }
        optato << "Case #" << i+1 << ": " << curarns << "\n";
    }
optato.close();
}
