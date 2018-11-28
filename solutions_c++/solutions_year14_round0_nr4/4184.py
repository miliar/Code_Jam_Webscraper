#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
    int T, N, cases=1;
    scanf("%d", &T);
    while(T--)
    {
        scanf("%d", &N);
        double naomi[N], ken[N];
        for(int i=0; i<N; i++)
            scanf("%lf", &naomi[i]);
        for(int i=0; i<N; i++)
            scanf("%lf", &ken[i]);
        sort(naomi, naomi+N);
        reverse(naomi, naomi+N);
        sort(ken, ken+N);
        reverse(ken, ken+N);

        int cnt1=0, ptr_l=0, ptr_r=(N-1);
        for(int i=(N-1); i>=0; i--)
        {
            if(naomi[i]<ken[ptr_r])
                ptr_l++;

            else
            {
                ptr_r--;
                cnt1++;
            }
        }

        bool vis[1007]={0};
        int cnt2=0, ptr=(N-1);
        for(int i=0; i<N; i++)
        {
            int turn=ptr;
            bool turn_done=false;
            for(int j=0; j<N; j++)
            {
                if(!vis[j] && ken[j]>naomi[i])
                {
                    turn=j;
                    turn_done=true;
                }
            }

            vis[turn]=true;
            if(!turn_done)
            {
                ptr--;
                turn=ptr;
                cnt2++;
            }
        }
        printf("Case #%d: %d %d\n", cases, cnt1, cnt2);
        cases++;
    }
    return 0;
}
