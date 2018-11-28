#include<iostream>
#include<string>
#include<cstring>
#include<fstream>
using namespace std;
int main(){
    ifstream fin;
    ofstream fout;
    fin.open ("B-small-attempt0.in");
    fout.open("output_PanCake.out");
    int T;
    fin>>T;
    int counter=0;
    while(counter<T){
        counter++;
        string panStack;
        fin>>panStack;
        fout<<"Case #"<<counter<<": ";
        int64_t panStackBinary=0;
        for(int index=0;index<panStack.length();index++){
            panStackBinary<<=1;
            if(panStack.at(index)=='-')
                panStackBinary|=1;
            else if(panStack.at(index)=='+')
                panStackBinary|=0;
        }
        int turns=0;
        int noOfTurns=0;
        while(panStackBinary && noOfTurns<panStack.length()){
            if(panStackBinary&1){
                panStackBinary=~panStackBinary;
                turns++;
            }
                panStackBinary>>=1;
                noOfTurns++;
        }
        fout<<turns<<endl;
    }
    fin.close();
    fout.close();
}
