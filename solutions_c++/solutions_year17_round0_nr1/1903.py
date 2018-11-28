#include<stdio.h>
#include<string.h>

int n,k;
int a[100005],m[100005];

int f(int x)
{
    int i,j,res=0;
    for(i=1;i<=n;i++)a[i]=m[i];
    for(i=1;i<=n-k+1;i++){
        if(a[i]!=x){
            for(j=i;j<i+k;j++){
                a[j]=1-a[j];
            }
            res++;
        }
    }
    for(i=1;i<=n;i++){
        if(a[i]!=x)return 1e9;
    }
    return res;
}

char b[100005];

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t,lt,res,i;
    char x;
    scanf("%d", &t);
    for(lt=1;lt<=t;lt++){
        scanf(" %s", b);
        n=strlen(b);
        for(i=1;i<=n;i++){
            x=b[i-1];
            if(x=='+')a[i]=0;
            else a[i]=1;
            m[i]=a[i];
        }
        scanf("%d", &k);
        res=f(0);
        printf("Case #%d: ", lt);
        if(res==1e9)printf("IMPOSSIBLE\n");
        else printf("%d\n", res);
    }
    return 0;
}
