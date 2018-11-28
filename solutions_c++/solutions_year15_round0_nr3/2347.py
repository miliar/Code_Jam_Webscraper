#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

#define MAX 10005


// ------------- global -------------
char valuesArray[MAX];
int nValues = 4;
char correspChar[4] = {'1', 'i', 'j', 'k'};
char mult[4][4] = {{1, 2, 3, 4},
                {2, -1, 4, -3},
                {3, -4, -1, 2},
                {4, 3, -2, -1}};
char allMult[MAX][MAX];

// ------------- functions -------------
char correspondingValue(char c){
    for(int i=0; i<nValues; i++)
        if(correspChar[i] == c)
            return (i+1);
    return -10;
}

// i*j
char multiply(char i, char j){
    bool neg = (i<0 && j>0) || (i>0 && j<0);
    return (neg ? -1 : 1)*(mult[abs(i)-1][abs(j)-1]);
}

// multiply elements in range [i, j)
void multiplyAll(int length){
    for(int i=0; i<length; i++){
        char v = valuesArray[i];
        allMult[i][i] = v;
        for(int j=i+1; j<length; j++){
            v = multiply(v, valuesArray[j]);
            allMult[i][j] = v;
        }
    }
}

bool tryCut(int i1, int i2, int length){
    char v = allMult[0][i1-1];
    if(v != 2) // 'i'
        return false;
    v = allMult[i1][i2-1];
    if(v != 3) // 'j'
        return false;
    v = allMult[i2][length-1];
    return (v == 4); // 'k'
}

// ------------- main -------------
int main () {
    int T;
    cin >> T;
    
    for(int i=0; i<T; i++){
        int L, X;
        cin >> L >> X;
        
        // fill valuesArray
        int length = X*L;
        char c;
        for(int j=0; j<L; j++){
            cin >> c;
            valuesArray[j] = correspondingValue(c);
        }for(int j=L; j<length; j++)
            valuesArray[j] = valuesArray[j%L];
        
        // calculate all multiplications => O(n^2)
        multiplyAll(length);
        
        // find a cut that works => O(n^2)
        bool isPossible = false;
        for(int j=1; j<length-1 && !isPossible; j++){
            for(int k=j+1; k<length && !isPossible; k++){
                isPossible = tryCut(j, k, length);
            }
        }
     
        cout << "Case #" << (i+1) << ": " << (isPossible ? "YES" : "NO") << endl;
    }

    return 0;
}
