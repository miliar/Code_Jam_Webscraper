#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include<cstdio>
#include<cmath>

using namespace std;



int main() {
    int TC;
    int casenum = 1;
    cin >> TC;
    while(TC--){
        int N;
        cin >> N;
        string line;
        cin >> line;
        int sum = 0;
        int m = 0;
        for(int i = 0; i < N+1; i++){
            
            if(sum < i) {
              m += i-sum;
              sum = i;
            }
            int n = line[i]- '0';
            sum += n;
        }
        cout << "Case #" << casenum++ << ": " << m << endl;
    }
    
}
