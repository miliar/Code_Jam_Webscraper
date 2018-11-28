#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int N, K, L, S, maxNum = 0;
string keys, target;

int get(int num, string s) {
    if (num == 0) {
        int counter = 0;
        //cout << s << endl;
        for (int i = 0; i < S - L + 1; i++) {
            bool possible = true;
            for (int j = 0; j < L; j++) {
                if (s[j+i] != target[j]) {
                    possible = false;
                    break;
                }
            }
            if (possible) counter++;
        }
        maxNum = max(maxNum, counter);
        return counter;
    }
    
    int val = 0;
    for (int i = 0; i < K; i++)
        val += get(num-1, s + keys[i]);
    return val;
}

int main() {
    ifstream cin("/Users/byunghoon/Desktop/Programs/Programs/in.txt");
    ofstream cout("/Users/byunghoon/Desktop/Programs/Programs/out.txt");
    
    cin >> N;
    
    for (int i = 0; i < N; i++) {
        cin >> K >> L >> S >> keys >> target;
        maxNum = 0;
        
        int ans = get(S, "");
        double final = 0;
        
        final = maxNum - ((double) ans / (double) pow(K, S));
        cout << "Case #" << (i+1) << ": " << setprecision(7) << final << endl;
    }
    
    return 0;
}