// Author:   Charles AUGUSTE

#include <iostream>
#include <fstream>
#include <math.h>
#include <sstream>
#include <stdlib.h>
#include <vector>
#include <Imagine/LinAlg.h>

using namespace std;

int main(){
    int T;
    cin >> T;
    for (int i=0; i<T; ++i){
        string ABC;
        cin >> ABC;
        int Q[27];
        for (int j=0; j<27; ++j){
            Q[j]=0;
        }
        for (int j=0; j<ABC.size(); ++j){
            Q[int(ABC[j]-64)]+=1;
        }
        cout << "Case #" << i+1 << ": ";
        for (int j=0; j<Q[26]; ++j){
            cout << 0;
        }
        for (int j=0; j<Q[15]-Q[18]-Q[23]-Q[7]+Q[8]; ++j){
            cout << 1;
        }
        for (int j=0; j<Q[23]; ++j){
            cout << 2;
        }
        for (int j=0; j<Q[8]-Q[7]; ++j){
            cout << 3;
        }
        for (int j=0; j<Q[18]-Q[26]-Q[8]+Q[7]; ++j){
            cout << 4;
        }
        for (int j=0; j<Q[6]-Q[18]+Q[26]+Q[8]-Q[7]; ++j){
            cout << 5;
        }
        for (int j=0; j<Q[24]; ++j){
            cout << 6;
        }
        for (int j=0; j<Q[19]-Q[24]; ++j){
            cout << 7;
        }
        for (int j=0; j<Q[7]; ++j){
            cout << 8;
        }
        for (int j=0; j<Q[9]-Q[24]-Q[6]-Q[8]-Q[26]+Q[18]; ++j){
            cout << 9;
        }
        cout << endl;
    }
    return 0;
}
