#include <cstdio>
#include <cstring>

using namespace std;

int main(void)
{
    int t, n, m, i, j, tc=0, res;
    bool valid[16];
    for (scanf("%d", &t);t--;)
    {
        res=-1;
        memset(valid, 0, sizeof(valid));
        for (i=0;i<2;i++)
        {
            scanf("%d", &n);
            for (j=0;j<16;j++)
            {
                scanf("%d", &m);
                if ((j>>2)==n-1)
                {
                    if (!i)
                        valid[m-1]=1;
                    else if (valid[m-1])
                        res=((res==-1) ? (m) : (0));
                }
            }
        }
        printf("Case #%d: ", ++tc);
        if (res>0)
            printf("%d\n", res);
        else
            printf("%s\n", ((res) ? ("Volunteer cheated!") : ("Bad magician!")));
    }
    return 0;
}
