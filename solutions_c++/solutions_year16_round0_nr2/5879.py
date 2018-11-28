#include <bits/stdc++.h>

using namespace std;
int cases = 1;
int main(void) {
    freopen("/home/vanessi/ClionProjects/CodeJamQB/Revenge of the Pancakes.in","r",stdin);
    freopen("/home/vanessi/ClionProjects/CodeJamQB/Revenge of the Pancakes.out","w",stdout);
    int t;
    scanf("%d", &t);
    while (t--) {
        char m [100];
        scanf("%s", &m);
        string in(m);
        int cnt = 0,fnd = 0;
        if(in[0]=='-')cnt++;
        else fnd = 1;
        for (int i = 1; i < in.length(); ++i) {
            if(in[i]=='+')fnd = 1;
            else if(fnd && in[i]=='-'&&in[i-1]=='+')cnt+=2;
        }
        printf("Case #%d: %d\n", cases++,cnt);
    }
}