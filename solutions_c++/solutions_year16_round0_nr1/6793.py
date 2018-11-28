#include <bits/stdc++.h>
using namespace std;
int t, n;
vector<int> seen;
int cnt, digit, num, cur;

void check(int x) {
    while(x != 0) {
        cur = x%10; 
        x/=10;   
        if(!seen[cur]) {
            seen[cur] = 1;
            cnt++;
        }
    }
}

int solve() {
    num = n;
    cnt = 0;
    while(cnt<10) {
        check(num);
        //printf("%d\n", num);
        if(cnt==10) return num;
        num += n;
    }
}

int main() {
    scanf("%d", &t);
    for(int _=1;_<=t;_++) {
        scanf("%d", &n);
        seen.assign(10, 0);
        if(n!=0) printf("Case #%d: %d\n", _, solve()); 
        else printf("Case #%d: INSOMNIA\n", _);
    }
}
