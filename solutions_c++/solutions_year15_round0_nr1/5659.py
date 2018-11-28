#include<cstdio>
#include<algorithm>

using namespace std;

int main()
{
    int t,it;
    scanf("%d",&t);
    it = t;
    while(t-- > 0)
    {
        int n;
        scanf("%d",&n);
        char s[1010];
        scanf("%s",s);
        int ans = 0;
        int run = s[0] - '0';
        for(int i=1;i<=n;i++)
        {
            if(run < i)
            {
                ans += i - run;
                run += i - run;
            }
            run += s[i] - '0';
        }
        printf("Case #%d: %d\n",it-t, ans);
    }
}
