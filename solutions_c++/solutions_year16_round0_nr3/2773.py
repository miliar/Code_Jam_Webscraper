
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

#define MAX 16

bool comp[1000];
vector<int> p;

int num[MAX];

void primes () {
    
    for (int i = 2; i < 1000; i++) {
        if (comp[i]) continue;
        p.push_back(i);
        for (int k = i+i; k < 1000; k += i)
            comp[k] = true;
    }
}

vector<int> divisor;
bool composite (lli n, int base) {
    for (int i = 0; i < p.size(); i++)
        if (n % p[i] == 0) {
            divisor.push_back(p[i]);
            return true;
        }
    return false;
}

lli convert (int base) {
    lli n = 0, p = 1;
    for (int i = MAX-1; i >= 0; i--) {
        n += num[i] * p;
        p *= base;
    }
    return n;
}

bool jamcoin () {
    divisor.clear();
    for (int b = 2; b <= 10; b++) {
        lli cur = convert(b);
        if (!composite(cur, b))
            return false;
    }
    return true;
}


int main() {
    
    ifstream fin ("input.txt");
    ofstream fout ("ans.txt");
    
    primes();
    
    lli T; cin >> T;
    for (lli t = 0; t < T; t++) {
        
        cout << "Case #" << t+1 << ": " << "\n";

        
        int N, J; cin >> N >> J;
        int total = 0;
        
        num[0] = num[MAX-1] = 1;
        
        for (int i = 1; i < MAX-1; i++) {
            num[i] = (num[i] + 1) % 2;
            for (int k = i+1; k < MAX-1; k++) {
                num[k] = (num[k] + 1) % 2;
            
                if (jamcoin()) {
                    total ++;
                    for (int j = 0; j < MAX; j++)
                        cout << num[j];
                    for (int j = 0; j < divisor.size(); j++)
                        cout << " " << divisor[j];
                    cout << "\n";
                    if (total >= J)
                        return 0;
                }
                
                num[k] = (num[k] + 1) % 2;
            }
            
            num[i] = (num[i] + 1) % 2;
        }
    }
    
    return 0;
}