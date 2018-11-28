#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
//#define SIZE 7
#define SIZE 40
using namespace std;

int main () {
    
    ifstream input ("A-large.in-2.txt");
    ofstream output ("output.txt");
    
    unsigned int count = 0;
    input >> count; cout << count << endl;

    unsigned int maxShy;
    string audience;
    
    unsigned int bring, up, position;
    char tmp;
    
    for (unsigned int i = 1; i <= count; i++) {
        maxShy = 0;
        input >> maxShy; cout << " " << maxShy << endl;

        getline(input, audience);//     cout << sizeof(audience) << endl;
        
        up = 0;    //how many have gone up
        bring = 0;
        position = 0;
        
        for (unsigned int shy = 0; shy <= maxShy; shy++) {
        
            tmp = audience[shy+1];
            position = atoi(&tmp);
            
            if (shy <= up) {
                
            } else if (up < shy) {
                bring += (shy - up);
                up += (shy - up);
            }
            up += position;
            
            //cout << audience[shy] << " ";
        }
        cout << "Case #" << i << ": " << bring << endl;
        
        output << "Case #" << i << ": " << bring << endl;
    }

    return 0;
}
