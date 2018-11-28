/* BEGIN_OF_SOURCE_CODE */
#include <iostream>
#include <fstream>
#include <sstream>  

#include <cstring> //for memset
#include <cstdio>
#include <cmath>

#include <algorithm>
#include <numeric>
#include <iterator>

#include <vector>
#include <list>
#include <string>

#include <queue>
#include <stack>

#include <utility>
#include <map>
#include <set>
#include <iomanip> //??

#define REP(i,n) for(int i=0;i<(n);++i) 

using namespace std; //change 

int T, A, N;
int res;
vector<int> nums;

void gao(int currA, int k, int noper) {
    if(k >= N) {
        if(noper < res) res = noper;
        return ;
    }

    if(currA > nums[k]) {
        gao(currA + nums[k], k+1, noper);
    } //prune
    else {
        int delta = currA - 1;
        //two candidate
        if(delta > 0) {
            gao(currA + delta, k, noper+1); //add
            gao(currA, k+1, noper+1); //remove
        }
        else
            gao(currA, k+1, noper+1); //remove
    }
    return ;
}

int main(void) {
    cin>>T;
    for(int i = 1; i <= T; ++i)  {
        cin>>A>>N;
        nums.resize(N);
        for(int j = 0; j < N; ++j) cin>>nums[j];
        res = 200;
        sort(nums.begin(), nums.end());
        gao(A, 0, 0);
        cout<<"Case #"<<i<<": "<<res<<endl;
    }   
    return 0;
}
/* @END_OF_SOURCE_CODE */
