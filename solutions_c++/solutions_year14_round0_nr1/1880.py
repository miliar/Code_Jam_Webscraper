#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <unordered_set>
#include <stdio.h>
#include <string.h>
#include <unordered_map>
#include <fstream>
using namespace std;

#define MOD 1000000007
#define ll long long

ifstream fin("in.txt");
ofstream fout("out.txt");

int main(){
    int t;
    fin>>t;
    for(int asdasd=0; asdasd<t; asdasd++){
        int rivi;
        fin>>rivi;
        unordered_set<int> overkill;
        for(int i=0; i<4; i++){
            for(int e=0; e<4; e++){
                int a;
                fin>>a;
                if(i+1==rivi)
                    overkill.insert(a);

            }
        }
        fin>>rivi;
        unordered_set<int> vastaus;
        for(int i=0; i<4; i++){
            for(int e=0; e<4; e++){
                int a;
                fin>>a;
                if(i+1==rivi)
                    if(overkill.count(a))
                        vastaus.insert(a);
            }
        }
        fout<<"Case #"<<asdasd+1<<": ";
        if(vastaus.size()>1)
            fout<<"Bad magician!"<<endl;
        if(vastaus.size()==1)
            fout<<*vastaus.begin()<<endl;
        if(vastaus.size()==0)
            fout<<"Volunteer cheated!"<<endl;
    }

    return 0;
}
