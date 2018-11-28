#include <iostream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <sstream>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>
#include <cstdlib>
#include <cstring>
#include <ctime>
using namespace std;
int dp[50];
int main() {
    int Case = 1;
    int t,i,j;
    long long  A,B,K;
    cin>>t;
    while(t--)
    {
        long long num = 0;
        for(i = 0; i < 40; i++)
            dp[i] = 0;
        
        cin>>A>>B>>K;
        for(i = 30; i >= 0;i --)
        {
            if((A> (1<<i))&&(B > (i<<i)))
            {
                if((1<<i)< K)
                {
                    num += ((1<<i) + 1)*((1<<i) + 1);
                }
            }
        }
        cout<<"Case #"<<Case++<<": "<<num<<endl;
    
    }
    
    return 0;
}
