
#include <fstream>
#include <iostream>
#include <algorithm>
#include <vector>
#include <math.h>
#include <iomanip>
#include <map>
using namespace std;
typedef long long ll;

#define MAX 1011
int shyness[MAX];

int main() {

    ofstream fout ("ans.txt");
    ifstream fin ("input.txt");
    
    int T;
    fin >> T;
       // TEST CASES
    for (int t = 0; t < T; t++) {
        int ans = 0;
        
        int N;
        fin >> N;
        
        string s; fin >> s;
        for (int i = 0; i <= N; i++)
            shyness[i] = s[i] - '0'; // there are s[i] people with shyness i
        
        int standup = 0; // current number of people standing.
        for (int i = 0; i <= N; i++) {
            if (standup >= i)
                standup += shyness[i];
            else if (shyness[i] != 0) {
                ans += i - standup;
                standup += i - standup;
                standup += shyness[i];
            }
         }
        
        
        fout << "Case #" << t+1 << ": " << ans << "\n";
    }
    
    return 0;
}

