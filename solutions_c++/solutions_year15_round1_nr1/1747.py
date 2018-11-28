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
    
    ll cases, ans;
    ll mushrooms, rate;
    vector<ll>mush;

    
    input>>cases;
    for (int c=0;c<cases;c++){
        output<<"Case #"<<c+1<<": ";
        input>>mushrooms;
        ans = 0;
        mush.clear();
        mush.resize(mushrooms);
        for (int i=0;i<mushrooms;i++){
            input>>mush[i];
        }
        
        for (int i=1;i<mushrooms;i++){
            if (mush[i] < mush[i-1]){
                ans += mush[i-1]-mush[i];
            }
        }
        output<<ans<<" ";
        ans = 0;
        rate = 0; //rate per 10
        for (int i=1;i<mushrooms;i++){
            if (mush[i] < mush[i-1]){
                if ((mush[i-1]-mush[i]) % 10 != 0){
                    rate = max(rate, (((mush[i-1]-mush[i]))));
                }
                else{
                    rate = max(rate, (((mush[i-1]-mush[i]))));
                }
            }
        }
        for (int i=1;i<mushrooms;i++){
            ans += min(rate, mush[i-1]);
        }
        output<<ans<<"\n";
        
        
    }
    
    return 0;
}
