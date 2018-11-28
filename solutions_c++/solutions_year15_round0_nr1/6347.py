#include <iostream>
#include <fstream>
#include <list>
using namespace std;

int main() {
    ifstream in("standing.in");
    ofstream out("standing.out");
    
    int K;
    in>> K;
    for(int k=0;k<K;k++) {
        int Smax;
        in >> Smax;
        list<pair<int, int> > standers;
        for(int i=0;i<=Smax;i++) {
            char c;
            in>>c;
            int count = c - '0';
            if(count != 0)
                standers.push_back(pair<int, int>(i, count));
        }
        int additonalNeeded = 0;
        int currentlyStanding = 0;
        for(auto iter = standers.begin(); iter != standers.end(); iter++) {
            int required = iter->first;
            if(required > currentlyStanding) {
                additonalNeeded += required - currentlyStanding;
                currentlyStanding = required;
            }
            currentlyStanding += iter->second;
        }
        out<<"Case #"<<(k+1)<<": "<<additonalNeeded<<"\n";
    }
    out.close();
    return 0;
}