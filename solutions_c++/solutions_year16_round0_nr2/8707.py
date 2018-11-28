#include <iostream>
#include <string>
using namespace std;


int main(){
    int cases;
    cin >> cases;
    string pile;
    int flipped;
    for (int c = 1; c <= cases; c++){
        cin >> pile;
        flipped = 0;
        for (int j = pile.length()-1; j >= 0; j--){
            if ( (pile[j] == '+') xor (flipped % 2 == 0) )
            {
                // meaning you need to flip it;
                flipped ++;
            }
        }
        cout << "Case #" << c << ": " << flipped << endl; 
    }    

    return 0;
}
