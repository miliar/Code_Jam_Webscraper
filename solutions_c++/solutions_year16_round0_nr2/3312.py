
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

int pos, ans;
string str;

bool iterate ()
{
    int len = int(str.length());
    
    while (pos < len && str[pos] == '+')
        pos++;
    
    if (pos >= len)
        return true;
    
    ans += 2;
    while (pos < len && str[pos] == '-')
        pos++;
    
    if (pos >= len)
        return true;

    return false;
}

int main() {
    
    ifstream fin ("input.txt");
    ofstream fout ("ans.txt");
    
    lli T; fin >> T;
    for (lli t = 0; t < T; t++) {
        
        fin >> str;
        pos = ans = 0;
        int len = int(str.length());

        while (pos < len && str[pos] == '-') pos ++;
        if (str[0] == '-') ans ++;
        
        while (!iterate()) {
        
        }
        
        fout << "Case #" << t+1 << ": ";
        fout << ans << "\n";
    }
    
    return 0;
}

