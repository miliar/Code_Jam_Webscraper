#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <string>

#define FI first
#define SE second
#define MP make_pair

using namespace std;

const int MAXN=104;

int tnum, n;
set<int> s;

void process(int x) {
    s.insert(x%10);
    x /= 10;
    if (x>0) process(x);
}

int main(){
    scanf("%d", &tnum);
    
    for (int t=1; t<=tnum; t++) {
        printf("Case #%d: ", t);
        scanf("%d", &n);
        if (n==0) {
            printf("INSOMNIA\n");
            continue;
        }
        s.clear();
        
        int ans = n;
        for (ans = n; ; ans+=n) {
            process(ans);
            if (s.size()==10) break;            
        }
        printf("%d\n", ans);
    }
    
	return 0;
}
