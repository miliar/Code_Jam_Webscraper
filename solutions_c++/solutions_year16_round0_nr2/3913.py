#include <bits/stdc++.h>

using namespace std;

bool check(int a[], int n)
{
    for(int i=0;i<n;i++)
        if(!a[i])
            return 0;
    return 1;
}

int main()
{
    int T;
    int a[110];
    freopen("in.in","r",stdin);
    freopen("out.txt","w",stdout);

    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        char str[110];
        scanf(" %s", str);

        printf("Case #%d: ",t);
        int n = strlen(str);
        for(int i=0;i<n;i++)
            if(str[i]=='+')
                a[i] = 1;
            else
                a[i] = 0;
        int c = 0;

        while(!check(a,n))
        {
            int l = 0;
            if(a[l])
                c++;
            while(l<n && a[l])
            {
                a[l] = 0;
                l++;
            }

            int r = n-1;
            while(r>-1 && a[r])
                r--;

            l = 0;
            while(l<=r)
            {
                int p = a[l];
                a[l] = (a[r]+1)%2;
                a[r] = (p+1)%2;
                l++;
                r--;
            }
            c++;
        }

        printf("%d\n",c);
    }
    return 0;
}
