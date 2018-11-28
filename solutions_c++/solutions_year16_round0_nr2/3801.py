#include <cstdio>
#include <cstring>
char a[110],b[110];
void show()
{
    for (int i=0;a[i];++i)
        printf("%c",a[i]);
    printf("\n");
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int testcase;
    scanf("%d\n",&testcase);
    for (int ii=1;ii<=testcase;++ii)
    {
        scanf("%s",a);
        int ans=0,top;
        for (top=0;a[top];++top);
        for (--top;top>=0 && a[top]=='+';--top);
        while (top>=0)
        {
            int wz=0;
            for (;a[wz]=='+';++wz);
            if (wz) ans+=1;
            for (int i=0;i<wz;++i)
                a[i]='-';
            ans+=1;
            memcpy(b,a,sizeof(a));
            for (int i=0;i<=top;++i)  // [0,top] flip
                if (b[top-i]=='+') a[i]='-';
                else a[i]='+';
            //show();
            for (--top;top>=0 && a[top]=='+';--top);
        }
        printf("Case #%d: %d",ii,ans);
        if (ii<testcase) printf("\n");
    }
    return 0;
}
