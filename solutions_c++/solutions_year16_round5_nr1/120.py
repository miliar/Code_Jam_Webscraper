#include<stdio.h>
#include<algorithm>
using namespace std;
char p[20100], st[20100];
int n, top;
int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int TC, TT, i, a, TTT, j, k, e, res;
    scanf("%d",&TC);
    for(TT=1;TT<=TC;TT++){
        printf("Case #%d: ",TT);
        scanf("%s",p+1);
        for(i=1;p[i];i++);
        n=i-1;
        top = 0;
        res = 0;
        for(i=1;i<=n;i++){
            if(top && st[top] == p[i]){
                top--;
                res++;
            }
            else{
                st[++top] = p[i];
            }
        }
        printf("%d\n",n*5 - (n/2 - res)*5);
    }
}
