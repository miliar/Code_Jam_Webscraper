#include <cstdio>
#include <cstring>

using namespace std;

void flip(char *s, int a, int b){
    char tmp[b-a];
    for(int i=a,c=0;i<b;i++,c++){
        tmp[c] = s[i] == '+' ? '-':'+';
    }
    for(int i=a,c=b-a-1;i<b;i++,c--){
        s[i] = tmp[c];
    }
}

int solve(char *s){
    int l = strlen(s);
    int c=0;
    while(1){
        while(s[l-1]=='+') l--;
        if(l==0) break;
        c++;
        if(s[0]=='-') flip(s, 0, l);
        else{
            int t=l;
            while(s[t-1]=='-') t--;
            flip(s,0,t);
        }
        //printf("%s\n",s);
    }

    return c;
}

int main()
{
    char s[110];
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        scanf("%s",s);
        printf("Case #%d: %d\n",i,solve(s));
    }
    return 0;
}
