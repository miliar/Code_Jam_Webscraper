
#include <iostream>
#include <string.h>
#include <stdio.h>
#include <set>
#include <cmath>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <stack>
#include <vector>
#include <algorithm>
#include <map>
#include <streambuf>
#include <sstream>
#include <queue>
#include <iomanip>
#define ll long long
#define INF 1e9
#define PI acos(-1.0)



using namespace std;



int main() {
freopen("B-large.in","r",stdin);
freopen("output.out","w",stdout);
int T;
scanf("%d",&T);
for(int t = 1 ; t <= T; t++) {
    char s[111];
    scanf("%s",s);
    int n = strlen(s);
    int i = n - 1;
    int ans = 0;
    if(n > 1) {
        while(i > 0) {
            if(s[i] != s[i-1])
                ans++;
            i--;
        }
    }
    if(s[n-1] == '-') ans++;
    printf("Case #%d: %d\n",t,ans);

}
  return 0;
}

