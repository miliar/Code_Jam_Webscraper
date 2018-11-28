#include <iostream>
#include <fstream>
#include <unistd.h>
using namespace std;

int main(int argc, const char * argv[]) {
    ifstream in;
    ofstream out;
    out.open("./result.txt");
    in.open("./A-small-attempt0.in.txt");
    if(!in.is_open() || !out.is_open()) {
        char * dir = getcwd(NULL, 0);
        cout << "file not opened." << dir;
        return -1;
    }
    int T;
    
    in >> T;
    
    for(int t = 0 ;t < T ; t++) {

        int smax = -1;
        in >> smax;
        
        int nPeopleStanding = 0;
        int nPeopleNeeded = 0;
        
        for(int i = 0; i < smax + 1 ; i++) {
            char n;
            in >> n;
            int nPeopleForI = n - '0';
            if(nPeopleForI == 0) continue;
            
            if(nPeopleStanding >= i) {
                nPeopleStanding += nPeopleForI;
            }
            else {
                int nPeopleToInvite = (i-nPeopleStanding);
                nPeopleStanding += nPeopleToInvite + nPeopleForI;
                nPeopleNeeded += nPeopleToInvite;
            }
            //cout << nPeopleStanding << endl;
        }
        
        out << "Case #" << t + 1 << ": " << nPeopleNeeded << endl;
    }
    
    return 0;
}
