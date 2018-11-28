#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

#define MAX 10000

int main () {
    int t;
    cin >> t;
    
    for(int i=0; i<t; i++){
        int shyMax;
        cin >> shyMax;
        
        //int* people = new int[shyMax];
        int people[MAX];
        int total = 0, invited = 0;
        for(int j=0; j<=shyMax; j++){
            char c;
            cin >> c;
            people[j] = c - '0';

            if(total < j){
                invited += j-total;
                total = j;
            }
            
            total += people[j];
        }
        
        cout << "Case #" << (i+1) << ": " << invited << endl;
        //delete[] people;
    }
    

    return 0;
}
