#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <time.h>
#include <assert.h>
#define MAXN 150001
using namespace std;

int t;

char flip(char a){
    return a == '-'? '+': '-';
}
int main(){
    freopen("/Users/Masoud/Desktop/A-large.in", "r", stdin);
    freopen("/Users/Masoud/Desktop/out.txt", "w", stdout);
    
    int ca = 1;
    scanf("%d", &t);
    while(t--){
        char str[1010];
        scanf("%s", str);
        string s = str;
        int k;
        scanf("%d", &k);
        int min_cnt = 0;
        for(int i=0; i<s.length(); i++){
            if(s[i] == '-'){
                if(i+k > s.length()){
                    min_cnt = -1;
                    break;
                }else{
                    min_cnt++;
                    for(int j=i; j<i+k; j++){
                        s[j] = flip(s[j]);
                    }
                }
            }
        }
        if (min_cnt == -1) {
            printf("Case #%d: IMPOSSIBLE\n", ca++);
        }else{
            printf("Case #%d: %d\n", ca++, min_cnt);
        }
    }
    return 0;
}




