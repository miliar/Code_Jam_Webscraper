#include <cstdio>

int main()
{
    FILE *fp = fopen("A-large.in", "r");
    FILE *ofp = fopen("output.txt", "w");
    int T;  fscanf(fp, "%d", &T);
    for(int t = 1; t <= T; ++t)
    {
        int n;  fscanf(fp, "%d", &n);
        int c[10] = {0};
        int cnt = 0;
        fprintf(ofp, "Case #%d: ", t);
        for(int i = n; i; i += n)
        {
            int j = i;
            while(i)
            {
                if(c[i%10] == 0)
                {
                    c[i%10] = 1;
                    cnt++;
                    if(cnt == 10)   break;
                }
                i /= 10;
            }
            if(cnt == 10)
            {
                fprintf(ofp, "%d\n", j);
                break;
            }
            i = j;
        }
        if(cnt != 10)
        {
            fputs("INSOMNIA\n", ofp);
        }
    }
    fclose(fp);
    fclose(ofp);
    return 0;
}
