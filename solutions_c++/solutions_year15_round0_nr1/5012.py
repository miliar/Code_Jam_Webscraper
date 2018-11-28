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
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;


int main() {
    freopen("/Users/vishnusankar/Desktop/CodeJam2015/input.in", "r", stdin);
    freopen("/Users/vishnusankar/Desktop/CodeJam2015/output", "w", stdout);
    int tc;
    scanf("%d", &tc);
    for (int i = 1;i <= tc;i++) {
        int maxShy = 0;
        scanf("%d", &maxShy);
        string shyCntStr;
        cin>>shyCntStr;
        unsigned int added = 0,clapped = 0;
        for(int j = 0; j < (maxShy + 1);j++){
            int numOfPeople = (shyCntStr[j] - '0');
            if(j == 0){
                clapped += numOfPeople;
            }else if(numOfPeople >= 1){
                if(clapped < j){
                    added += (j - clapped);
                    clapped += (j - clapped);
                }
                clapped += numOfPeople;
            }
        }
        printf("Case #%d: %d\n",i,added);
    }
    return 0;
}
