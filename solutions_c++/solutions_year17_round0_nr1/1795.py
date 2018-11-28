#include <algorithm>
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <vector>
using namespace std;
ifstream in("A-small.in");
ofstream out("out.out");
vector<bool> pancakes;

bool isCorrect(){
    for (int i=0;i<pancakes.size();i++)
        if (!pancakes.at(i))
            return false;
    return true;
}

int main()
{
    int caso,ncasi,k;
    in>>ncasi;
    char pan;
    for (caso=1;caso<=ncasi;caso++){
        pancakes.clear();
        pan=in.get();
        pan=in.get();
        do{
            pancakes.push_back(pan=='+');
            pan=in.get();
        } while (pan!=' ');
        in>>k;
        int i,j;
        for (i=0;!isCorrect();i++){
            for (j=0;pancakes.at(j);j++);
            if (j+k>pancakes.size()) {
                i=-1;
                break;
            }
            for (int z=0;z<k;z++)
                pancakes.at(j+z)=!pancakes.at(j+z);
        }
        if (i==-1){
            out<<"Case #"<<caso<<": "<<"IMPOSSIBLE"<<endl;
        } else {
            out<<"Case #"<<caso<<": "<<i<<endl;
        }
    }
    return 0;
}
