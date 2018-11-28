#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

void print_ans(FILE *ofp, int t, int ans)
{
    if(!ofp)
    {
        printf("Case #%d: %d\n", t, ans);
        return;
    }
    fprintf(ofp, "Case #%d: %d\n", t, ans);
}

void flip(int b, char* str)
{
    for(int i = 0; i <= b; ++i) {
        str[i] = (str[i] == '-' ? '+' : '-');
    }
}

int main()
{
    FILE *fp = fopen("B-large.in", "r");
    FILE *ofp = fopen("output.txt", "w");
    int T;  fscanf(fp, "%d", &T);
    for(int t = 1; t <= T; ++t)
    {
        char S[200];
        fscanf(fp, "%s", S);
        int i, j, cnt = 0;
        int n = strlen(S);
        for(i = n; i >= 0; --i)
        {
            if(S[i] == '-') break;
        }
        n = i;
        while(n >= 0)
        {
            i = n;
            for(j = i - 1; j >= 0; --j)
            {
                if(S[j] == '+') break;
            }
            flip(i, S);
            cnt++;
            n = j + 1;
            if(n == 0)  break;
        }
        print_ans(ofp, t, cnt);
    }
    fclose(fp);
    fclose(ofp);
    return 0;
}
