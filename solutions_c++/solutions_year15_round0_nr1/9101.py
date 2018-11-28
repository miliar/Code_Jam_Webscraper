#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int main()
{
    int n;
    freopen("A-large.in","r",stdin);
    scanf("%d", &n);
    char a[1010];
    freopen("A-small-attempt0.out","w",stdout);
    for(int i=0;i<n;i++)
    {
        int p;  scanf("%d", &p);
        scanf("%s", a);
        int s=0,br=0;    int l=strlen(a);
        for(int i=0;i<l;i++)
        {
            if(s<i && a[i]!='0')
            {
                br+=i-s;
                s=i;
            }
            s+=a[i]-'0';
        }
        printf("Case #%d: %d\n", i+1,br);
    }


    return 0;
}
