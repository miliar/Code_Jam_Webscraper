#include <iostream>
#include <cstdio>
using namespace std;
int cnt[13][3];
bool greaterstr(char* str, int st, int lmid, int mid, int ed)
{
    for (int i=0; i<= lmid - st; i++)
        if (str[i+st] > str[i+mid])
            return true;
        else if (str[i+st] < str[i+mid] )
            return false;
    return false;
}
void process(char * str, int st, int ed)
{
    if (st == ed)
        return;

    int mid = (ed-st+1)/2 + st;
    process(str, st, mid-1);
    process(str, mid, ed);
    if (greaterstr(str, st, mid-1, mid, ed))
    {
        for (int j=st;j<mid;j++)
            swap(str[j], str[mid-st+j]);
    }
}
int main()
{
    cnt[0][0] = 1;
    cnt[0][1] = 1;
    cnt[0][2] = 0;
    for (int i=1; i<=12; i++)
    {
        cnt[i][0] = cnt[i-1][0] + cnt[i-1][2];
        cnt[i][1] = cnt[i-1][1] + cnt[i-1][0];
        cnt[i][2] = cnt[i-1][2] + cnt[i-1][1];
    }

    int tt;
    cin >> tt;
    char str[4] = "SPR";
    //printf("%d %d %d",cnt[11][0],cnt[11][1],cnt[11][2]);
    for (int tc=1;tc<=tt;tc++)
    {
        int n,c[3];
        cin >> n >> c[2] >> c[1] >>c[0];
        printf("Case #%d: ",tc);
        int flag=0;
        for (int i=0;i<3;i++)
        {
            if (cnt[n-1][0] == c[i] && cnt[n-1][1] == c[(i+1)%3] && cnt[n-1][2] == c[(i+2)%3])
            {
                flag = 1;
                int output[10000];
                output[0] = i;
                output[1] = (i+1)%3;
                int topidx = 2;
                for (int i=1; i<n; i++)
                {
                    int oriidx = topidx;
                    for (int j=0; j<oriidx; j++)
                        output[topidx++] = (output[j]+1)%3;
                }
                char outstr[10000];
                for (int i=0;i<topidx;i++)
                    outstr[i] = str[output[i]];
                outstr[topidx] = '\0';
                process(outstr, 0, topidx-1);
                printf("%s\n",outstr);
                break;
            }
        }
        if (!flag)
            printf("IMPOSSIBLE\n");
    }

    return 0;
}
