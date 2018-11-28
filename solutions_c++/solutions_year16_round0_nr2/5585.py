#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;
int h[110];
int b[110];
int main (){
    b[1]=1;
    h[1]=0;
    for(int i = 2 ; i < 100 ; i ++){
        b[i]=h[i-1]+1;
        h[i]=b[i-1]+1;
    }
    int T;
    scanf("%d",&T);
    for(int I = 1 ; I <= T ; I++ ){
        char s[200];
        scanf("%s",s);
        int len=strlen(s);
        bool first=s[0]=='+';
        bool pre=first;
        int cnt=1;
        for(int i = 1 ; i < len ; i ++){
            bool now=s[i]=='+';
            if(now!=pre){
                pre=now;
                cnt++;
            }
        }
        if(first)printf("Case #%d: %d\n",I,h[cnt]);
        else printf("Case #%d: %d\n",I,b[cnt]);
    }

}
