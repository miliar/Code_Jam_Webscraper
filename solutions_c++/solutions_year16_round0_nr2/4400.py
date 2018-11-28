#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int tests;
char pancake[112345];
int n;
bool is_happy() {

    for(auto x:pancake) {
        if(x=='-') return false;
    }
    return true;
}


void flip(int k) {
    stack<char> stk;
    for(int i=0; i<=k; i++) {
        if(pancake[i]=='-')stk.push('+');
        else stk.push('-');
    }
    int y=k;
    while(!stk.empty()) {
        pancake[y--]=stk.top();
        stk.pop();
    }
}


int main() {
    freopen("B-large.in","r",stdin);
    freopen("sabbir.txt","w",stdout);
    scanf("%d ",&tests);
    for(int t=1; t<=tests; t++) {
        scanf("%s",pancake);
        n=strlen(pancake);
        int ans=0;
        while(!is_happy()) {
            ans++;
            if(pancake[0]=='-') {
                int j=n-1;
                while(pancake[j]=='+') {
                    j--;
                }
                flip(j);

            } else {
                int j=0;
                while(pancake[j]=='+') {
                    j++;
                }
                j--;
                flip(j);
            }

        }
        printf("Case #%d: %d\n",t,ans);
    }
}
