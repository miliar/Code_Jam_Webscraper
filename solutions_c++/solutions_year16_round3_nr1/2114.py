#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>

using namespace std;

void solve(int P[], int N);
int main()
{
    int T;
    int cnt=1;
    scanf("%d", &T);
    while (cnt <= T)
    {
        int N;
        int P[30]={0};
        scanf("%d", &N);
        for(int i=0; i<N; i++)
        {
            scanf("%d", &P[i]);
        }
        printf("Case #%d: ", cnt);
        solve(P, N);
        cnt++;
    }

    return 0;
}

void solve(int P[], int N)
{
    int sum = 0;
    for(int i=0; i<N; i++)
    {
        sum = sum + P[i];
    }
    if(sum%2==1)
    {
        int maxP = 0;
        int Pi = 0;
        for(int i=0; i<N; i++)
        {
            if(P[i]>maxP)
            {
                maxP = P[i];
                Pi = i;
            }
        }
        printf("%c ", ((char)Pi+'A'));
        P[Pi] = P[Pi] - 1;
        sum = sum - 1;
    }
    while(sum != 0)
    {
        int maxP = 0;
        vector<int> Pi;
        for(int i=0; i<N; i++)
        {
            if(P[i]>maxP)
            {
                maxP = P[i];
                Pi.clear();
                Pi.push_back(i);
            }
            else if(P[i]==maxP)
            {
                Pi.push_back(i);
            }
        }
        if(Pi.size()%2 == 0)
        {
            printf("%c%c ", ((char)Pi[0]+'A'), ((char)Pi[1]+'A'));
            P[Pi[0]] = P[Pi[0]] - 1;
            P[Pi[1]] = P[Pi[1]] - 1;
        }
        else
        {
            printf("%c%c ", ((char)Pi[0]+'A'), ((char)Pi[0]+'A'));
            P[Pi[0]] = P[Pi[0]] - 2;
        }
        sum = sum - 2;
    }
    printf("\n");
}

