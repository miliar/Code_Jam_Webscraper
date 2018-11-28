#include <cstdio>
#include <utility>
#include <algorithm>
#include <vector>
#include <iostream>
#define MAX_N 1001
using namespace std;

int maxi[MAX_N], suma, supposed, temp;
int testCases;
string caso[MAX_N];
int main(){
    cin >> testCases;
    for (int i = 0; i < testCases; i++) {
        cin >> maxi[i];
        cin >> caso[i];
        suma = 0, supposed = 0;
        for(int j = 0; j< maxi[i]; j++){
            suma += caso[i][j]-'0';
            while(suma < j+1){suma+=1;supposed+=1;}
        }
        cout << "Case #" << i+1 <<": "<<supposed << endl;;
    }
    
}