#include <cassert>
#include <cstdio>
#include <iostream>
#include <string>
using namespace std;
int countConsecutive(string pancakes, char temp);
void flipAndReverse(string& pancakes, int index);
int countReverse(string pancakes, char temp);
int main(){
    FILE *fin = freopen("B-large.in", "r", stdin);
    assert(fin!=NULL);
    FILE *fout = freopen("B-large.out", "w", stdout);
    int cases;
    cin >> cases;
    for (int i = 0; i < cases; i++){

        string pancakes;
        cin >> pancakes;
        cout << "Case #" << i+1 << ": ";
        int totalFlips = 0;
        for (int i = pancakes.length()-1; i > 0 ; i--){
            if (pancakes[i] != pancakes[i-1]){
                totalFlips+=1;
            }
        }
        if (pancakes[pancakes.length()-1] == '-')
            totalFlips+=1;

        cout << totalFlips << endl;
    }
}
