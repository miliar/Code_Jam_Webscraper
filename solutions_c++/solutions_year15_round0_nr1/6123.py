#include <cstdio>
#include <algorithm>
int c=0;
void run(){
    int n,cur=0,ans = 0;
    char s[1005];
    scanf ("%d",&n);
    scanf ("%s",s);
    for (int i=0;i<=n;i++){
        s[i] -= '0';
        if (cur<i)
            ans += i-cur,cur = i;
        cur += s[i];
    }
    printf ("Case #%d: %d\n",c,ans);
}

int main(){
freopen ("A-large.in","r",stdin);
freopen ("out.txt","w",stdout);
    int testnum;
    scanf ("%d",&testnum);
    while (testnum--){
        c++;
        run();
    }

return 0;
}
