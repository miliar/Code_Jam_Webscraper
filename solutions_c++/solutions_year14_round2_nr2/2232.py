#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <string>
#include <queue>
#include <stack>
#include <cmath>
using namespace std;
int main(int argc, char **argv)
{
    int T;
    cin >> T;
    for(int cas = 1; cas <= T; cas ++){
        int A, B, K;
        int bits[1000];
        cin >> A >> B >> K;
        int sum = 0;
        for(int a = 0; a < A;  a++){
            for(int b = 0; b< B; b++){
                int c = a & b;
                if(c < K){
                    sum ++;
                }
            }
        }
        cout << "Case #" << cas << ": " << sum << endl; 
    }
    return 0;
}

