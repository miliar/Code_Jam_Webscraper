#include<iostream>
#include<set>
#include<queue>
#include<bitset>
#include<assert.h>
using namespace std;


int main() {

   int numCase = 1000000;
    cin >> numCase; 
    for (int i = 0; i < numCase; i++) {
        int K, C, S;
        cin >> K;
        cin >> C;
        cin >> S;
        cout <<"Case #"<<(i+1)<<": ";
        for (int j = 1; j <= S; j++)
            cout << " " << j;
        cout << endl; 
    }
}
