#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<vector>
#include <cmath>

using namespace std;
#define Fill(a, b) memset(a, b, sizeof(a))
#define Debug(x) cout<<#x<<"="<<(x)<<endl;
typedef long long LL;


int main()
{
    int i = 0, j = 0, kase = 0;
    int n, t;
    LL num;
    int flag[15];
    FILE *fp = fopen("out.txt", "w");
    FILE *fp2 = fopen("in.txt", "r");
    fscanf(fp2, "%d", &t);
    while(t--)
    {
        fscanf(fp2, "%I64d", &num);
        if(num == 0)
        {
            fprintf(fp, "Case #%d: INSOMNIA\n", ++kase);
            continue;
        }
        int sum = 0;
        LL ans = 0;
        Fill(flag, 0);
        while(1)
        {
            if(sum >= 10)
                break;
            ans += num;
            LL tmp = ans;
            while(tmp)
            {
                int a = tmp%10LL;
                if(!flag[a])
                {
                    flag[a] = 1;
                    sum++;
                }
                tmp = tmp/10LL;
            }
        }
        fprintf(fp, "Case #%d: %I64d\n", ++kase, ans);
    }
    fclose(fp);

    return 0;
}






















