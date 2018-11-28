#include<stdio.h>
#include<fstream>
#include<string.h>
using namespace std;
FILE *fin=fopen("A-large.in","r");
FILE *fout=fopen("A-large.out","w");
int t, n;
char s[1010];
int main()
{
    int i, j=0, x, ans;
    fscanf(fin, "%d", &t);
    while(fscanf(fin, "%d", &n)!=EOF)
    {
        ++j;
        x=ans=0;
        fscanf(fin, "%s", s);
        for(i=0; i<=n; ++i)
        {
            if(x<i){ ++ans; ++x; }
            x+=s[i]-'0';
        }
        fprintf(fout, "Case #%d: %d\n", j, ans);
    }
}
