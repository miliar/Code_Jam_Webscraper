#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
int n;
int p[20];
int now[20];
char s[20];
bool check[15];
main()
{
    int time,counter = 1;
    int i,k,ans;
    FILE* fi = fopen("A-large.in","r");
    FILE* fo = fopen("sheep_out.txt","w");
    fscanf(fi,"%d",&time);
    while(time--)
    {
        memset(p,0,sizeof(p));
        memset(now,0,sizeof(now));
        memset(check,0,sizeof(check));
        fscanf(fi," %s",s);
        fprintf(fo,"Case #%d: ",counter++);
        if(s[0]=='0')
        {
            fprintf(fo,"INSOMNIA\n");
            continue;
        }
        ans = 0;
        n = strlen(s);
        for(i=0;i<n;i++)
        {
            now[i] = p[i] = s[n-i-1] - '0';
            if(!check[p[i]]) ans++;
            check[p[i]] = true;
        
        }
        while(ans!=10)
        {
            for(i=0;i<n;i++) 
            {
                p[i] += now[i];
                if(p[i]>9)
                {
                    p[i+1] += p[i]/10;
                    p[i] %= 10;
                    n = max(n,i+2);
                }
                if(!check[p[i]]) ans++;
                check[p[i]] = true;
            }
        }
        for(i=n-1;i>=0;i--) fprintf(fo,"%d",p[i]);
        fprintf(fo,"\n");
    }
    scanf(" ");
}
