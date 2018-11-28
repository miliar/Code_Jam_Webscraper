#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <math.h>
#include <fstream>
using namespace std;
int minutesNeeded(multiset<int> initialplates){
    int totalPlates=initialplates.size();
    int smallest=*(initialplates.rbegin());
    //cout << *(initialplates.rbegin()) << endl;
    for(int goal=1; goal <=*(initialplates.rbegin()); goal++){
    //cout << goal << endl;
        int loops=0;
        auto current=initialplates.rbegin();
        for(int i=totalPlates-1; i >= 0 && *current > goal; current++, i--){
        //cout << i << endl;
            loops+=round(ceil(((float) (*current))/((float) (goal))))-1;
        }
        //cout << " " << loops << endl;
        loops+=goal;
        if(loops<smallest){
            smallest=loops;
        }
    }
    return smallest;
}
int main(int argv, char* arguements[])
{
    fstream input;
    input.open(arguements[1]);
    int total;
    input >> total;
    for(int i=0; i<total; i++){
        int totalPlates;
        input >> totalPlates;
        multiset<int> plates;
        for(int q=0; q<totalPlates; q++){
            int current;
            input >> current;
            plates.insert(current);
           // cout << current << " ";
        }
        //cout << endl;
        cout << "Case #" << i+1 << ": " << minutesNeeded(plates) << endl;
    }
    return 0;
}
