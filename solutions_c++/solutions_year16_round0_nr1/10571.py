#include <cmath>
#include <cstdio>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
using namespace std;

int main()  {
    freopen("A-large.in", "r", stdin);
    freopen("out1.txt", "w", stdout);
    int tt; cin>>tt;
    
    for(int i=1;i<=tt; ++i)  {
        set<char> num;
        int res=0;
        
        int n; cin>>n;
        int j=1;
        if(n==0) {
            printf("Case #%d: INSOMNIA\n", i);
            fflush(stdout);
            continue;
        }
        bool done=false;
        while(true) {
            int m = n * j++;
            string s = to_string(m);
            for(char c:s) num.insert(c);
            if(num.size() == 10) {res=m; break;}
        }
        
        printf("Case #%d: %d\n", i,res);
        fflush(stdout);
    }
    return 0;
}