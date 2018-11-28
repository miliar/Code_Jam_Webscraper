//Template of CyberKasumi (Jennifer Santoso a.k.a. Liang Qiuxia)

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
#include <cstring>
#include <queue>
using namespace std;

#define LL long long
#define inf 2123123123
#define MOD 1000000007


int a;
LL b;
LL c;
vector<LL>vec;
vector<int>digit;
bool palin(LL x){
    LL p=x;
    digit.clear();
    while(p>0){
        digit.push_back(p%10);
        p/=10;
    }
    int ea=digit.size();
    for (int i=0;i<ea/2;i++){
        if (digit[i]!=digit[ea-i-1]){
            return false;
        }
    }
    return true;
}
int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    vec.push_back(-1);
    for (int i=1;i<10000000;i++){
        if (palin(i) && palin(i*i)){
            vec.push_back(i*i);
        }
    }
    vec.push_back(212312312312312312ll);
    scanf("%d",&a);
    for (int z=1;z<=a;z++){
        cin >> b >> c;
        int t=0;
        int atas,bawah;
        while(vec[t]<b)t++;
        bawah=t;
        t=0;
        while(vec[t]<=c)t++;
        atas=t;
        printf("Case #%d: %d\n",z,atas-bawah);
    }
    //while(1);
    return 0;
}
