#include <iostream>
#include <string>
using namespace std;

int main(){
    int t;
    int flips;
    char o, p;
    cin >> t;
    string line;
    getline(cin, line);
    for(int c = 1; c <= t; c++){ 
        flips = 0;
        getline(cin, line);
        for(int i = 0; i < line.length() - 1; i++){
            if(line[i] != line[i+1]){
                flips++;
            }
        }
        if(line[line.length() - 1] == '-'){
            flips++;
        }
        cout << "Case #" << c << ": " << flips << endl;
    }
    return 0;
}
