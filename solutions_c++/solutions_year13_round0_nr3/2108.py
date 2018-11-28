#include <cmath>
#include <ctime>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <functional>
#include <algorithm>
#include <iostream>
#include <numeric>
#include <iomanip>
#include <sstream>
#include <bitset>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <list>
#include <set>
#include <map>
using namespace std;

#define debug(args...) fprintf(stderr,args)
#define foreach(_it,_v) for(typeof(_v.begin()) _it = _v.begin(); _it != _v.end(); ++_it)

typedef long long lint;
typedef pair<int,int> pii;
typedef pair<lint,lint> pll;

const int INF = 0x3f3f3f3f;
const lint LINF = 0x3f3f3f3f3f3f3f3fll;

bool isPalindrome(int n) {
    string s1 = "";
    while(n) {
        s1 += n%10+'0';
        n /= 10;
    }
    string s2 = s1;
    reverse(s2.begin(),s2.end());
    return s1 == s2;
}

int main() {
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;++t) {
        int l,r;
        scanf("%d%d",&l,&r);
        int root = 1;
        int ans = 0;
        for(int n=l;n<=r;++n) {
            while(root*root < n) root++;
            if(root*root != n) continue;
            if(isPalindrome(root) && isPalindrome(n)) ans++;
        }
        printf("Case #%d: %d\n",t,ans);
    }            
    return 0;
}
