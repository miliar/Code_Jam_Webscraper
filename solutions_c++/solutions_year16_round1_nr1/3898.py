#include <bits/stdc++.h>
using namespace std;

void solve()
{
    char a[1001],i=1,b[1001]="a";
    cin>>a;
    b[0]=a[0];
    b[1]='\0';
    for(int i=1;i<strlen(a);i++)
    {
        char c[1001]={a[i]};
        if(b[0]>a[i])
            strcat(b,c);
        else
        {
            strcat(c,b);
            strcpy(b,c);
        }
    }
    printf("%s \n",b);
}

int main()
{
    int n;
    scanf("%d", &n);
    for(int i=0;i<n;i++)
    {
    printf("Case #%d: ", i + 1);
    solve();
    }
    return 0;
}
