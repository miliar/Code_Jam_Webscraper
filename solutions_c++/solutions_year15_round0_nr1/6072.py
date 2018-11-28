#include <iostream>
#include <cstdio>
#include <algorithm>
#include <sstream>
#include <cstring>
#include <string>
#include <math.h>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <list>
#define MOD 1000000007
#define MAXN 25
using namespace std;
int n ,m,t;


int main (){
    freopen("/Users/Masoud/Desktop/in.txt", "r", stdin);
    freopen("/Users/Masoud/Desktop/out.txt", "w", stdout);
    int ca=1;
    scanf("%d",&t);
    while(t--){
        int si;
        scanf("%d",&si);
        char str[si+5];
        scanf("%s",str);
        int cur = str[0]-'0';
        int res=0;
        for(int i =1;i<=si;i++){
            if(cur<i&&(str[i]-'0')){
                res+=i-cur;
                cur+=(i-cur);
            }
            cur+=str[i]-'0';
        }
        printf("Case #%d: %d\n",ca++,res);
    }
    
    return 0;
}
