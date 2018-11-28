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

const long long maxn = 100000000000008;
long long T, A, B;
set<long long> nums;


bool isPar(long long num) {
    string s;
    stringstream strstream;
    strstream<<num;
    strstream>>s;
    
    bool flag = true;
    int len = s.size();
    int rig = (len - 2) / 2;
    len --;
    for(int i = 0; flag && i <= rig; ++i) {
        if(s[i] != s[len-i]) flag = false;
    }

    return flag;
}

void initialize() {

    long long i;
    for(i = 1; i <= 10000000; ++i) {
        if( isPar(i) && isPar( i * i) ) 
            nums.insert(i * i);
    }
    return ;
}

int main(void) {
    cin>>T;
    initialize();
    for(int i = 1; i <= T; ++i) {
        cin>>A>>B;
        cout<<"Case #"<<i<<": ";
        long long nofnums = 0;
        set<long long>::iterator itr = nums.begin();
        while(itr != nums.end()) {
            if( *itr >= A && *itr <= B ) nofnums++;
            ++itr;
        }
        cout<<nofnums<<endl;
    }
    return 0;
}
