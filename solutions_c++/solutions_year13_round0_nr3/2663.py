#include <cstdlib>
#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <limits.h>
#include <math.h>

using namespace std;
int isPal(unsigned long long n) {
    char buf[101];
    int count = snprintf(buf, 100, "%llu", n);
    int found = 1;
    for (int c = 0; c < count; c++) {

        if (buf[c] != buf[count - c - 1]) {
            found = 0;
            return 0;
        }
    }
    
    return 1;
}
int main(int argc, char** argv) {
    int cases;
    cin >> cases;

    for (int i = 1; i <= cases; i++) {
        unsigned long long from=0, to=0;
        cin >> from; cin>>to;
        
        int runs =1000;
        unsigned long long range = ULLONG_MAX/runs;
        
        unsigned long long nums  = 0;
        for(int r=0; r < to/range +1; r++){
            unsigned long long current = r * range;
            unsigned long long current_max = current + range;
            if(current < from)
                current =from;
            if(current_max > to){
                current_max = to;
            }
//            char* flags = (char*)calloc(sizeof(char), range);
//            cout << "checkiing range: " << current << " to " << current_max<<endl;
            unsigned long long square = 0;
            for(int n =sqrt(current); ; n++) {
                square = n * n;
                if(square < current)
                    continue;
                if(square > current_max)
                    break;
//                cout << "checkiing square: " << square << endl;
                
                if(isPal(n) == 1 && isPal(square))
                        nums ++;
//                cout << "count " << nums <<endl;
            }
        }
        
        cout << "Case #" << i << ": " << nums << endl;

    }
    return 0;
}

