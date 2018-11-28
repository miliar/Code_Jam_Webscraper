#include <iostream>
#include <fstream>
#include <limits.h>

using namespace std;

int P[1010];

int main()
{
    int T;
    ifstream in("D:/B-large.in");
    ofstream out("D:/B-large.out");
    in >> T;
    for(int ci=1; ci<=T; ci++){
        int D;
        in >> D;
        int pmax = 0;
        for(int i=0; i<D; i++){
            in >> P[i];
            pmax = max(pmax, P[i]);
        }
        int mintime = INT_MAX;
        int currtime;
        for(int i=1; i<=pmax; i++){
            currtime = i;
            for(int j=0; j<D; j++){
                int currp = P[j];
                while(currp > i){
                    currp -= i;
                    currtime ++;
                }
            }
            mintime = min(mintime, currtime);
        }
        out << "Case #" << ci << ": " << mintime << endl;
    }
    return 0;
}
