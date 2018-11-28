
#include <fstream>
#include <iostream>
#include <algorithm>
#include <vector>
#include <math.h>
#include <map>
using namespace std;
typedef long long ll;

#define MAX 10000
int mushroom[MAX];

int main() {

    ofstream fout ("ans.txt");
    ifstream fin ("input.txt");

    
    int T;
    fin >> T;
       // TEST CASES
    for (int t = 0; t < T; t++) {
        //int ans = 0;
        
        int N;
        fin >> N;
        for (int i = 0; i < N; i++)
            fin >> mushroom[i];
        
        // method 1.
        int y = 0;
        for (int i = 1; i < N; i++) {
            if (mushroom[i] < mushroom[i-1])
                y += mushroom[i-1] - mushroom[i];
        }
        
        // method 2.
        int z = 0;
        int diff = 0;
        for (int i = 0; i < N; i++) {
            if (mushroom[i-1] - mushroom[i] > diff)
                diff = mushroom[i-1] - mushroom[i];
        }
        
        for (int i = 0; i < N; i++) {
            if (mushroom[i-1] - diff >= 0)
                z += diff;
            else
                z += mushroom[i-1];
        }
        
        fout << "Case #" << t+1 << ": " << y << " " << z << "\n";
    }
    
    return 0;
}

