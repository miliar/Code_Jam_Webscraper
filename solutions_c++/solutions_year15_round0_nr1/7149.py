#include <cstdio>
#include <cstring>

int ctoi(char c)
{
    return c - '0';
}

int main()
{
    int TC,smax,len,ans,amt;
    char s[1010];
    scanf("%d",&TC);
    for(int TC_ = 1;TC_ <= TC;TC_++)
    {
        scanf("%d",&smax);
        scanf("%s",s);
        len = strlen(s);
        ans = amt = 0;
        for(int i = 0;i < len;i++)
        {
            if(i > 0)
                amt += ctoi(s[i-1]);
            if(amt < i)
                ans += i - amt,amt = i;
        }
        printf("Case #%d: %d\n",TC_,ans);
    }

    return 0;
}
