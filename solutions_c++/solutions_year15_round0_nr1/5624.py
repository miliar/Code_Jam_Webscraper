#include <iostream>
#include <cstdio>
#include <algorithm>
#include <utility>
#include <vector>
#include <cstdlib>
#include <string>
#include <cmath>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <iterator>
#include <iomanip>
#include <limits.h>
#define debug(v) for(long long int i=0;i<v.size();++i)cout<<v[i]<<" ";cout<<endl;
using namespace std;
int main(){
	freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    long long int t;
    cin >> t;
    for(long long int q = 1;q <= t;++q){
        long long int sMax;
        cin >> sMax;
        string order;
        cin >> order;
        vector<long long int> shy;
        for(long long int i=0;i<order.length();++i)
            shy.push_back((long long int)(order[i]-48));
        long long int called = 0,stood = shy[0];
        for(long long int i=1;i<shy.size();++i){
            if(i <= stood)
                stood += shy[i];
            else
                while(i > stood)
                    called += 1,stood += shy[i],stood += 1;
        }
        cout << "Case #" << q << ": " << called << endl;
    }
   	return 0;
}
