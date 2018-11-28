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
using namespace std;
int n,m;
int dp[9999991];
int get_last_num(int num){
    int inc=num;
    int cnt=0;
    while(cnt<((1<<10)-1)){
        int tmp=num;
        while (tmp) {
            int idx= tmp%10;
            tmp/=10;
            cnt|=(1<<idx);
        }
        num+=inc;
    }
    return num-inc;
}
int T;
int main (){
    freopen("/Users/Masoud/Desktop/A-large.in.txt", "r", stdin);
    freopen("/Users/Masoud/Desktop/out.txt", "w", stdout);
    
    scanf("%d",&T);
    for(int t=1;t<=T;t++){
        int num;
        scanf("%d",&num);
        printf("Case #%d: ",t);
        if (!num) {
            printf("INSOMNIA\n");
        }else{
            printf("%d\n",get_last_num(num));
        }
    }
    return 0;
}