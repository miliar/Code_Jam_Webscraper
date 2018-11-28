#ifndef BULLEYE_H
#define BULLEYE_H


#include <fstream>
#include <cstring>
#include <math.h>
using namespace std;

ifstream be_input;
ofstream be_output;

int radius, paint;
int be_num_cases;

void bulleye(){
    be_input.open("test.txt");
    be_output.open("be_output");
    be_input >> be_num_cases;
    cout << be_num_cases << endl;

    for(int i = 0; i < be_num_cases; i++){
        be_input >> radius;
        be_input >> paint;

        int num_cycles = 0;
        int needed_paint = 2 * radius + 1;
        while(paint >= needed_paint){
            paint -= needed_paint;
            radius += 2;
            needed_paint = 2 * radius + 1;
            num_cycles++;
        }

        be_output << "Case #" << i + 1 << ": " << num_cycles << endl;
    }
}

#endif
