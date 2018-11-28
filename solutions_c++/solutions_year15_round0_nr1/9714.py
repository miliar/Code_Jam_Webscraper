#include<cstdio>
//int find_next(int i, char s[])
//{
//    do{}while(s[i++] != '0');
//    return i-1;
//}
int main()
{
    int t, p = 0, smax, ans;
    FILE *fin, *fout;
    char s[1000];
    fin = fopen("A-small-attempt3.in","r");
    fout = fopen("A.out","w");
    fscanf(fin,"%d",&t);
    for(int j=1;j <= t;j++)
    {
        p = 0; ans = 0;
        //scanf("%d%s",&smax,s);
        fscanf(fin,"%d%s",&smax,s);
        for(int i = 0; i <= smax; i++)
        {
            if(s[i] == '0') continue;
            //printf("%d %d\n",i,p);
            if(p < i)
            {
                //printf("\n%d %d\n\n", i, p);
                ans += (i - p);
                p += (i - p);
            }
            p += (s[i] - '0');
        }
        //printf("Case #%d: %d\n",j,ans);
        fprintf(fout,"Case #%d: %d\n",j,ans);
    }
    fclose(fin);
    fclose(fout);
    return 0;
}
