
#include <iostream>
#include <fstream>
#include <algorithm>
#include <iomanip>
#include <math.h>
#include <stack>
#include <map>
#include <vector>
using namespace std;
typedef long long int lli;

#define MAX 101
bool met[10];

bool get_digits (lli n) {
    
    while (n > 0) {
        met[n%10] = true;
        n /= 10;
    }
    for (lli i = 0; i < 10; i++)
        if (!met[i]) return false;
    return true;
}

int main() {
    
    ifstream fin ("input.txt");
    ofstream fout ("ans.txt");
    
    lli T; fin >> T;
    for (lli t = 0; t < T; t++) {
        
        lli N, cur; fin >> N;
        cur = N;
        
        if (N == 0)
        {
            fout << "Case #" << t+1 << ": INSOMNIA\n";
            continue;
        }
        
        memset(met, 0, sizeof(met));
        while (!get_digits(cur))
            cur += N;
        
        fout << "Case #" << t+1 << ": ";
        fout << cur << "\n";
    }
    
    return 0;
}

