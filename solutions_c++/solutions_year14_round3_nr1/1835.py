#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <queue>
using namespace std;

char s[111];

int gcd(int x,int y){
    if (y) return gcd(y,x%y); else return x;
}

int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int T;
    cin>>T;
    gets(s);
    for (int _=1;_<=T;_++){
        int p=0,q=0,x;
        gets(s);
        x=0;
        for (;(s[x]!='/');x++) p=p*10+(s[x]-'0');
        x++;
        for (;x<strlen(s);x++) q=q*10+(s[x]-'0');
        x=q/gcd(p,q);
        int tot=0,cnt=0;
        while (x){
            tot++;
            if (x%2) cnt++;
            x/=2;
        }
        if (cnt!=1){printf("Case #%d: impossible\n",_); continue;}
        x=p/gcd(p,q);
        int ans;
        while (x){
            x/=2;
            tot--;
            if (x%2) ans=tot;
        }
        printf("Case #%d: %d\n",_,tot);
    }
//system("pause");
}
/*
7
1/2
3/4
1/4
2/23
123/31488
1/8
1/1

*/
