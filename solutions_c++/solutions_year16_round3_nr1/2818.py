#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <time.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <unordered_map>

#define INF 1000000000;
#define bitcount                    __builtin_popcount
#define gcd                         __gcd
#define EPS                         1e-9
#define all(a)                      a.begin(), a.end()

using namespace std;
typedef long long LL;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

priority_queue<int> store;

int main(){
    freopen("A-large.in","r",stdin);
    int tc,tcount=1,n,cur;
    scanf("%d\n",&tc);
    for(;tcount<=tc;tcount++){
        scanf("%d\n",&n);
        int count=0;
        for(int i=0;i<n;i++){
            scanf("%d",&cur);
            store.push(cur*100+i);
            count+=cur;
        }
        printf("Case #%d:",tcount);
        if(count%2==1){
            int first = store.top();
            store.pop();
            printf(" %c",'A'+(first%100));
            if(first>199)
                store.push(first-100);
        }
        while(!store.empty()){
            int first = store.top();
            store.pop();
            printf(" %c",'A'+(first%100));
            if(first>199)
                store.push(first-100);
            int second = store.top();
            store.pop();
            printf("%c",'A'+(second%100));
            if(second>199)
                store.push(second-100);
        }
        printf("\n");
    }
}