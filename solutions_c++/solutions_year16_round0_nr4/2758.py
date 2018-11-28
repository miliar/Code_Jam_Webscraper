#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int tt=1;tt<=t;tt++)
    {

        int k,c,s;
        cin >> k >> c >> s;
        printf("Case #%d: ",tt);
        for (int i=1;i<=s;i++)
        {
            printf("%d ",i);
        }
        printf("\n");
    }
    return 0;
}
