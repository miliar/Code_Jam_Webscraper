#include<cstdio>
#include<cstring>
using namespace std;
int Q,n,a,b,t;
int main()
{
    freopen("input","r",stdin);
    freopen("output","w",stdout);
    scanf("%d\n",&Q);
    while(t<Q)
    {
        t++;
        printf("Case #%d: ",t);
        scanf("%d %d %d",&n,&a,&b);
        if(a*b%n!=0||n>=7)printf("RICHARD\n");
        else if(n==1||n==2)printf("GABRIEL\n");
        else if(n==3)
        {
            if(a==1||b==1)printf("RICHARD\n");
            else printf("GABRIEL\n");
        }
        else if(n==4)
        {
            if(a<=2||b<=2)printf("RICHARD\n");
            else printf("GABRIEL\n");
        }
    }
    return 0;
}
