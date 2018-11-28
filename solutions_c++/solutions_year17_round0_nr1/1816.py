#include <bits/stdc++.h>

using namespace std;

int T, C=1, n, k;
char s[1024];

void flipa(int a, int b) {
    for (int i=a;i<=b;i++)
        if (s[i]=='-')
            s[i]='+';
        else
            s[i]='-';
}

int main() {

    for(scanf("%d",&T);T--;) {
        printf("Case #%d: ",C++);
        scanf("%s %d",s,&k);
        n = strlen(s);
        int resp=0;
        for (int i=0;i+k-1<n;i++)
            if (s[i]=='-') {
                resp++;
                flipa(i,i+k-1);
            }
        bool ok=true;
        for (int i=0;i<n;i++)
            if (s[i]=='-') {
                ok=false;
                break;
            }
        if (!ok)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n",resp);
    }

    return 0;
}
