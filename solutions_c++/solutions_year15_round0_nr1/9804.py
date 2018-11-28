#include <stdio.h>
#include <iostream>
#include <string.h>
#include <string>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <fstream>

using namespace std;

int main(){
    ifstream fin;
    ofstream fout;
    fin.open("A-small-attempt1.in");
    fout.open("A-small-result.txt");
    int T;
    int S;
    fin>>T;
    for(int i=1;i<=T;i++){
        fin>>S;
        char list[S];
        fin>>list;
        int no_of_people=0;
        int req=0;
        for(int j=0;j<=S;j++){
            int sVal = (int)(list[j]-'0');
            if(sVal!=0 && j>no_of_people)
            {
                req=req+(j-no_of_people);
                no_of_people+=req;
            }
            no_of_people+=(int)(list[j]-'0');
        }
        fout<<"Case #"<<i<<": "<<req<<endl;
    }
    return 0;
}

