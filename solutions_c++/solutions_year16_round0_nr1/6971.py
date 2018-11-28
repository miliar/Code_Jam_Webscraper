#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef unsigned long long ull;

int main() {
    freopen("/Users/vivekp/Downloads/A-large.in", "r", stdin);
    freopen("/Users/vivekp/Desktop/output", "w", stdout);
    int tc;
    cin>>tc;
    map<int,bool> nums;
    bool arr[10];
    for (int i = 1;i <= tc;i++) {
        ull n,cnt = 1,res;
        cin>>n;
        nums.clear();
        memset(arr,0,sizeof(arr));
        if(n == 0){
            cout<<"Case #"<<i<<": INSOMNIA"<<endl;            
            continue;
        }
        while(nums.size() != 10){
            ull s = n * cnt;
            while(s > 0){
                int digit = s % 10;
                if(arr[digit] == 0){
                    nums.insert(pair<int,bool>(digit,1));
                    arr[digit] = 1;
                    if(nums.size() == 10){
                        res = n * cnt;
                        break;
                    }
                }
                s /= 10;
            }
            cnt++;
        }
        cout<<"Case #"<<i<<": "<<res<<endl;
    }
    return 0;
}
