//
//  standing_ovation.cpp
//  A Standing Ovation
//

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main(int argc, const char * argv[]) {
    
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");
    
    int T;
    fin >> T;
    fin.ignore();
    
    for (int test_case_number = 1; test_case_number <= T; test_case_number++) {
     
        int Smax;
        fin >> Smax;
        fin.ignore();
        
        int people_standing = 0;
        int friends = 0;
        
        char c;
        int Si;
        for (int shyness = 0; shyness <= Smax; shyness++) {
            fin.get(c);
            Si = c - '0';
            
            if (people_standing < shyness) {
                // need to add (shyness - people_standing) further friends (with a lower shyness level than shyness)
                int new_friends = shyness - people_standing;
                people_standing += new_friends;
                friends += new_friends;
            }
            people_standing += Si;
        }
        
        fout << "Case #" << test_case_number << ": " << friends << endl;
    }
    
    fin.close();
    fout.close();
    
    return 0;
}
