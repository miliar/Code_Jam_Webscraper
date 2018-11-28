#include <iostream>
#include <math.h>
#include <algorithm>
#include <vector>
#include <sstream>
#include <string.h>
#include <fstream>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <tuple>
#include <iomanip>
#define ull unsigned long long
#define ll long long
#define inf 1000000000000
#define bil 1000000000

using namespace std;

ifstream input;
ofstream output;



int main(int argc, char *argv[]) {
    cin.sync_with_stdio(false);
    cout.sync_with_stdio(false);
    input.sync_with_stdio(false);
    output.sync_with_stdio(false);
    input.open("/users/jihan/Algorithmic Programming/CodeForces/B261/B261/B261.in.txt");
    output.open("/users/jihan/Algorithmic Programming/CodeForces/B261/B261/B261.out.txt");
    ll cases;
    ll rows, col, wid, ans;
    
    input>>cases;
    for (int c=0;c<cases;c++){
        output<<"Case #"<<c+1<<": ";
        input>>rows>>col>>wid;
        ans = 0;
        ans = col/wid;
        ans += wid-1;
        output<<ans<<"\n";
            
        
    }
    
    
    return 0;
}
