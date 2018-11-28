#include <cstdio>
#include <cstdlib>
#include <cmath>

using namespace std;

int main() {
    freopen("in","r",stdin);
    freopen("out","w",stdout);
    int cases;
    scanf("%d", &cases);
    for (int c=0; c<cases; ++c)
    {
        int maxshy;
        scanf("%d", &maxshy);
        char *shy = new char[maxshy];
        scanf("%s", shy);

        int count = 0;
        int extra = 0;
        for (int i=0; i<maxshy; ++i)
        {
            if (shy[i]-'0' == 0)
            {
                if (extra == 0)
                {
                    count++;
                }
                else
                {
                    extra--;
                }
            }
            else
            {
                if (shy[i]-'0' > 1) extra += (shy[i]-'0')-1;
            }
        }
        printf("Case #%d: %d\n", c+1, count);
        delete [] shy;
    }
}