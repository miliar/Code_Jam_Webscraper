#include <algorithm>
#include <cassert>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <string>
#include <unordered_set>
#include <vector>

using namespace std;

int A[1002];
//int S[1002];

int main(int argc, const char * argv[]) {
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small.out","w",stdout);
    
    int T = 0;
    cin >> T;
    int caseNum = 0;
    
    while (T--) {
        int ans = 0;
        int N;
        string str;
        cin >> N >> str;

        int k = 0;
        for (const char& c: str) {
            A[k++] = c - '0';
        }
        
        int sum = A[0];
        for (int i = 1; i <= N; i++) {
            if (i > sum) {
                ans++;
                sum++;
            }
            
            sum += A[i];
        }
        
        cout << "Case #" << ++caseNum << ": " << ans <<  "\n";
    }
    
    return 0;
}
