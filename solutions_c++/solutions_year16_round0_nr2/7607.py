#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

char s[1024];
int T, C=1, n, resp;

void inverte(int t) {
    for (int i=0;t-1-i>=i;i++) {
        swap(s[i], s[t-1-i]);
        s[i] = (s[i]=='+'?'-':'+');
        if (t-1-i != i)
            s[t-1-i] = (s[t-1-i]=='+'?'-':'+');
    }
}

int main() {

    for(scanf("%d",&T);T--;) {
        printf("Case #%d: ",C++);
        scanf("%s",s);
        n = strlen(s);
        resp = 0;
        while (n > 0) {
   //         printf("%s (%d)\n",s,resp);
            if (s[n-1]=='+') {
                n--;
                continue;
            }
            if (n==1) {
                resp++;
                inverte(1);
                n--;
                continue;
            }
            // se o primeiro for -
            if (s[0]=='-') {
                inverte(n);
                resp++;
                continue;
            }
            // achar ultimo +
            int pmais=-1;
            for (int i=0;i<n;i++)
                if (s[i]=='+') {
                    pmais=i;
                }
            // soh tem -?
            if (pmais==-1) {
                inverte(n);
                resp++;
                continue;
            }
            inverte(pmais+1);
            inverte(n);
            resp+=2;
        }
            //printf("%s (%d)\n",s,resp);
        printf("%d\n", resp);
    }

    return 0;
}
