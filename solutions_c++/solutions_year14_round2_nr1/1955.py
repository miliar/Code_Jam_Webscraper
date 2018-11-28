#include<cstring>
#include<cstdio>
using namespace std;

struct myString
{
    char s[105];
};

myString getOrder(myString x)
{
    myString y;
    int i,j=0;
    char c;

    y.s[0] = x.s[0];
    for(i=1;x.s[i]!='\0';i++)
    {
        if(x.s[i]!=y.s[j])
            y.s[++j] = x.s[i];
    }
    y.s[j+1] = '\0';
    return y;
}

int mod(int a)
{
    if(a<0)
        return -a;
    return a;
}

void getRL(int *x, char *s)
{
    int i,j=0;

    x[0]=1;
    for(i=1;s[i]!='\0';i++)
    {
        if(s[i] == s[i-1])
            x[j]++;
        else
            x[++j] = 1;
    }
}

int main()
{
//    freopen("input.txt","r", stdin);
    int i,j,n,t;
    myString str[105];
    myString order, temp;
    int ans,l;
    int arr[105][105];

    scanf("%d",&t);

    for(i=0;i<t;i++)
    {
        scanf("%d",&n);
        for(j=0;j<n;j++)
        {
            scanf("%s", &str[j].s);
        }

        order = getOrder(str[0]);
//        printf("order = %s\n", order.s);
        for(j=1;j<n;j++)
        {
            if(strcmp(order.s, getOrder(str[j]).s) != 0)
            {
                printf("Case #%d: Fegla Won\n", i+1);
                break;
            }
        }
        if(j != n)
            continue;
        l = strlen(order.s);
        for(j=0;j<n;j++)
        {
            getRL(&arr[j][0], str[j].s);
        }
        ans = 0;
        for(j=0;j<l;j++)    //small test case have N=2
        {
            ans = ans + mod(arr[0][j]-arr[1][j]);
        }
        printf("Case #%d: %d\n", i+1, ans);
    }
    return(0);
}
