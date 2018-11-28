#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <sstream>
#include <unordered_set>

using namespace std;

int solve(int N)    {
    unordered_set<int> digits;
    unordered_set<int> nums;

    for(int i=1; ; i++) {
        int R = N*i;

        if(nums.find(R) != nums.end())
            return -1;

        nums.insert(R);

        int x=R;
        while(x>0) {
            int r = x%10;
            digits.insert(r);
            x = x / 10;
        }

        if(digits.size() == 10)
            return R;

    }

}

int main(int argc, char *argv[])
{
    freopen("sheep-big.in","r",stdin);
    freopen("sheep-big.out","w",stdout);

    int T = 0;
    scanf("%d", &T);

    for(auto t=0; t < T; t++)  {
        printf("Case #%d: ", t+1);

        int N=0;
        scanf("%d", &N);

        int res=solve(N);

        if(res > -1)
            printf("%d\n",res);
        else
            printf("%s\n","INSOMNIA");
    }


    return 0;
}
