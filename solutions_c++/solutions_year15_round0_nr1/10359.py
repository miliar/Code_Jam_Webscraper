#include <iostream>
#include <fstream>

using namespace std;
int calculateMin(int si, int people, int prevTotal, int added);

int main(int argc, const char * argv[]) {
    
    ifstream inputf ("/Users/ash_ap/Google Drive/Code/A-small-attempt0.in");
    ofstream outputf ("/Users/ash_ap/Google Drive/Code/A-small-attempt0.out");
    string line;
    int smax, shy, friends, clap, lines;
    
    if (inputf.is_open()) {
        getline(inputf, line);
        lines = atoi(line.substr(0,3).c_str());
        
        for (int j = 0; j < lines; j++) {
            clap = 0;
            friends = 0;
            getline(inputf, line);
            smax = atoi(line.substr(0,1).c_str());
            
            for (int i = 0; i < smax+1; i++) {
                shy = atoi(line.substr(2+i, 1).c_str());
                
                if (i < clap + friends) friends += 0;
                else friends += i - (clap + friends);
                
                clap += shy;
            }
            outputf << "Case #" << j+1 << ": " << friends << '\n';
        }
    }
    
    else cout << "WHAT?!";
    
    return 0;
}