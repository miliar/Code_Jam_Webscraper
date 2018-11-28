#include<iostream>
#include<cstdio>
#include<cmath>

using namespace std;

int p[100];
long long a, b;

bool palindrome(long long x) {
    int cs = 0;
    while (x > 0) {
        p[cs] = x%10;
        x = x/10;
        cs++;
    }
    for(int i=0; i<cs/2; i++) {
       if (p[i] != p[cs-i-1]) return false;
    }
    return true;
}

int main() {
    int ntest;
    freopen("c.in", "r", stdin);
    freopen("c.txt", "w", stdout);
    
    scanf("%d", &ntest);
    
    long long x;
    
    for(int test=0; test<ntest; test++) {
        cout << "Case #" << test+1 << ": ";
        scanf("%d%d", &a, &b);
        int ans = 0;
        for(int i = min(1, (int)(sqrt(a))-1); i<= (int)sqrt(b)+1; i++) 
        if (palindrome(i)) {
            x = i*i;
            if (x < a || x>b)
                continue;
            if (palindrome(x)) {
                ans++;
                //cout << x << " ";
            }
        }
        cout << ans;
        cout << endl;
    }
    
    return 0;
}
