#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

#define MAX 10
int pancakes[MAX];

// ------------- global -------------

// ------------- functions -------------
int bestTime(int maxVal){
    if (maxVal <= 3)
        return maxVal;

    int t = maxVal, split = 0, pieces = 0;
    for(int i=2; i <= maxVal/2; i++){
        int v = pancakes[maxVal], v2 = maxVal;
        pancakes[maxVal - i] += v;
        pancakes[i] += v;
        pancakes[maxVal] = 0;

        while(pancakes[maxVal] == 0)// && maxVal >= 0)
            maxVal--;
        
        int newT = v + bestTime(maxVal);
        // cout << "new time = " << newT << " for split in " << i << " and " << maxVal-i << endl;
        if(t > newT){
            t = newT;
            split = i;
            pieces = v;
        }
        
        // restore previous state
        maxVal = v2;
        pancakes[v2 - i] -= v;
        pancakes[i] -= v;
        pancakes[maxVal] = v;
    }
    
    /*
    for(int j=0; j <= maxVal; j++)
        cout << "(" << j << ", " << pancakes[j] << ") ";
    cout << endl;
    cout << "maxVal = " << maxVal << ", split " << pieces << " (or " << pancakes[maxVal] << ") pieces of " << maxVal << " in " << split << " and " << maxVal-split << endl;
    */
    return t;
}

// ------------- main -------------
int main () {
    int T;
    cin >> T;
    
    for(int i=0; i<T; i++){
        for(int j=0; j < MAX; j++)
            pancakes[j] = 0;
            
        int D;
        cin >> D;
        
        int maxVal = 0;
        for(int j=0; j<D; j++){
            int value;
            cin >> value;
            pancakes[value]++;
            if(value > maxVal)
                maxVal = value;
        }
        
        int time = bestTime(maxVal);
        cout << "Case #" << (i+1) << ": " << time << endl;
    }

    return 0;
}
