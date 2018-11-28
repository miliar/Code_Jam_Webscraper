#include<cstdio>
#include<cstring>

int main()
{
    int T;
    scanf("%d", &T);
    for(int i=0; i<T; ++i)
    {
        int l;
        int p_num = 1;
        int ans;
        char S[100+1];
        scanf("%s", S);
        l = strlen(S);
        for(int j=0; j<l-1; ++j) if(S[j]!=S[j+1]) p_num++;
        if(S[0]=='+') ans = (p_num&1)?(p_num-1):p_num;
        else ans = (p_num&1)?p_num:(p_num-1);
        printf("Case #%d: %d\n", i+1, ans);
    }
    return 0;
}
