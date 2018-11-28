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
    
    int cases, tmp, answer, cur;
    string s;
    input>>cases;
    for (int i=0;i<cases;i++){
        answer = cur = 0;
        input>>tmp>>s;
        output<<"Case #"<<i+1<<": ";
        for (int j=0;j<s.size();j++){
            tmp = s[j]-'0';
            if (cur < j)  answer += (j-cur), cur = j;
            cur += tmp;
        }
        output<<answer<<"\n";
        
    }


    
    return 0;
}
