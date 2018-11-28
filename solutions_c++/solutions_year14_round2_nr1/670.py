#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

const int MAXL = 105,MAXN = 105;
char str[MAXL],lc[MAXL];
int val[MAXL][MAXN];

int main()
{
    int tnum;
    scanf("%d",&tnum);
    for(int t = 1; t <= tnum; t++)
    {
        printf("Case #%d: ",t);
        int n;
        scanf("%d",&n);
        
        bool flag = true;
        int m = 0;
        for(int i = 0; i < n && flag; i++)
        {
            scanf("%s",str);
            
            int len = strlen(str),p,j;
            for(p = 0,j = 0; j < len; p++)
            {
                if (i == 0) lc[p] = str[j];
                else if (lc[p] != str[j]) 
                {
                    flag = false;
                    break;
                }
                
                int c = 0;
                for(; j < len && str[j] == lc[p]; j++,c++);
                val[p][i] = c;
            }
            
            if (i == 0) m = p;
            else if (m != p) 
            {
                flag = false;
            }
        }
        
        if (flag)
        {
            int ans = 0;
            for(int i = 0; i < m; i++)
            {
                sort(val[i],val[i] + n);
                int mid = val[i][n / 2];
                for(int j = 0; j < n; j++) 
                    ans += abs(val[i][j] - mid);
            }
            printf("%d\n",ans);
        }
        else puts("Fegla Won");
    }
    return 0;
}
