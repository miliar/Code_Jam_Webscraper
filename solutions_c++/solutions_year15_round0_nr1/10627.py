//#include <cstdlib>
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <sstream>
//#include <time.h>

using namespace std;

bool clap(int maxShy, string people, int noShy = 0) {
    int k = 0;
    int aux;
    
    for (int i = 0; i < people.length(); i++) {
        
        if (k > maxShy)
            k = maxShy;
        
        aux = atoi(people.substr(i, 1).c_str());

        if (noShy >= k || aux == 0)
            noShy += aux;
        else
            return false;
        k++;
    }
    
    return true;
}


int main(int argc, char** argv) {
    
    int cases;
    int max;
    int noShy;
    string people;
    
    /*
    if (clap(1, "09"))
        cout << "ok";
    else
        cout << "mal";
    return 0;
    */
    
    scanf("%d", &cases);
    
    for (int i = 0; i < cases; i++) {
        
        scanf("%d ", &max);
        getline(cin, people);
        
        noShy = 0;
        do {
            
            if (clap(max, people, noShy))
                break;
            noShy++;
            
        } while(true);
        
        printf("Case #%d: %d\n", i + 1, noShy);
    }
    
    return 0;
}