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
int T;
int main (){
    freopen("/Users/Masoud/Desktop/B-large.in-2.txt", "r", stdin);
    freopen("/Users/Masoud/Desktop/out.txt", "w", stdout);

    cin>>T;
    for(int t=1;t<=T;t++){
        string s;
        cin>>s;
        int ans=0;
        int i=0;
        while (i<s.length()) {
            if (s[i]=='-') {
                ans+=2;
            }
            int j=i;
            while (j<s.length()&&s[j]==s[i]) {
                j++;
            }
            i=j;
        }
        if (s[0]=='-') {
            ans--;
        }
        printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}