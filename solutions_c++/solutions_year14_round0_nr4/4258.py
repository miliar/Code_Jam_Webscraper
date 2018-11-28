#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

double val[2][1000];
bool used[2][1000];
int main()
{
    int TC;
    scanf("%d", &TC);

    for(int tc = 1; tc <= TC; ++tc)
    {
        int N;
        scanf("%d", &N);
        int deceitful = 0, nonDeceitful = 0;

        for(int i = 0; i < 2; i++)
        {
            for(int j = 0; j < N; j++)
                scanf("%lf", &val[i][j]);
            sort(val[i], val[i]+N);
        }
       
        memset(used, 0, sizeof(used)); 
        for(int i = N-1; i >= 0; i--)
        {
            bool findFlag = false;
            for(int j = 0; j < N; j++)
                if(!used[1][j] && val[1][j] > val[0][i])
                {
                    used[1][j] = true;
                    findFlag = true;
                    break;
                }

            if(!findFlag)
            {
                for(int j = 0; j < N; j++)
                    if(!used[1][j])
                    {
                        used[1][j] = true;
                        break;
                    }
                ++nonDeceitful;
            }
        }
        
        memset(used, 0, sizeof(used));
        for(int i = 0; i < N; i++)
        {
            int j = 0;
            while(used[1][j]) ++j;

            if(val[0][i] > val[1][j])
            {
                used[1][j] = true;
                ++deceitful;
            }
            else //eliminate the highest
            {
                j = N-1;
                while(used[1][j]) --j;
                used[1][j] = true;
            }
        }
        printf("Case #%d: %d %d\n", tc, deceitful, nonDeceitful);        
    }
    return 0;
}
