/* 
 * File:   main.cpp
 * Author: Timo
 *
 * Created on 9. huhtikuutata 2016, 21:21
 */

#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    //ifstream ifs("input.txt");
    //ifstream ifs("B-small-attempt0.in");
    ifstream ifs("B-large.in");
    ofstream ofs("output.txt");
    
    int T;
    ifs >> T >> ws;
    
    for(int test=1; test<=T; test++) {
        ofs << "Case #" << test << ":";
        cout << "Case #" << test << ":";
        
        string line;
        getline(ifs, line);
        //cout << line << endl;
        
        int n=0;
        int s=0;
        
        bool up = true;
        if(line[0] == '-') up = false;
        
        for(int i=0; i<line.size()-1; i++)
            if(line[i] != line[i+1]) {s++; up = !up;};
        n += s;
        if(!up) n++;
        
        ofs << " " << n << endl;
        cout << " " << n << endl;
        
        
    }
    
    return 0;
}

