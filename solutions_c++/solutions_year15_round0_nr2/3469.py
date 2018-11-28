#include <iostream>
#include <set>
#include <algorithm>
#include <iterator>
#include <cmath>
#include <tuple>
#include <stack>
#include <iomanip>
#include <string>
#include <vector>
#include <queue>
 
 
using namespace std;
 
int main(int, char** ){
    cin.tie(nullptr); ios::sync_with_stdio(false);
    //cout << fixed <<  std::setprecision(10) ;
    int t;
    cin >> t;
    for(int i = 0; i < t; ++i){
        int d;
        cin >> d;

        vector<int> pi(d);
        for(int j = 0; j < d; ++j){
            cin >> pi[j];
        }
        sort(pi.rbegin(), pi.rend());

        int ans = 114514;

        for(int j = pi[0]; 0 < j; --j){
            //cout << j << ":";
            int buf = 0;
            for(int k : pi){
                if(k<=j) break;
                //cout << k << " ";
                buf+=k/j;
                if(k%j==0) --buf;
            }
            buf+=j;
            //cout << "->" << buf << endl;
            ans=min(ans,buf);
        }

        cout << "Case #" << i+1 << ": " << ans << endl;
    }
    return 0;
}