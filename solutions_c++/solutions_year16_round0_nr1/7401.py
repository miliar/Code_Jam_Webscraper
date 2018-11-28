//
//  QA-large.cpp
//  CodeJam2016
//
//  Created by Ha Young Park on 4/9/16.
//  Copyright © 2016 Ha Young Park. All rights reserved.
//

#include <fstream>
#include <set>

using namespace std;

int main(int argc, const char * argv[]) {
    ifstream fin;fin.open("A-large.in");
    ofstream fout;fout.open("A-large.out");
    
    int T;
    fin >> T;
    
    for(int i = 1; i <= T; i++){
        unsigned long N;
        set<unsigned long> digits;
        
        fin >> N;
        unsigned long k = N;
        
        for(k = N; k != 0; k += N) {
            unsigned long j = k;
            while(j > 0){
                digits.insert(j % 10);
                j /= 10;
            }
            
            if(digits.size() == 10)
                break;
            
        }
        
        fout << "Case #" << i << ": ";
        if(k == 0)
            fout << "INSOMNIA" << endl;
        else
            fout << k << endl;
    }
    
    fout.close();fin.close();
    
    return 0;
}

