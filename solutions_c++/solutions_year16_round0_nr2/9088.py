#include <bits/stdc++.h>
using namespace std;
long long int t=0;
char d[110][110];
void flip(long long int x,long long int y,long long int l)
{
    long long int p=x,q=y;
    while(x<=y)
    {
        char temp=d[l][x];
        d[l][x]=d[l][y];
        d[l][y]=temp;
        x++;
        y--;
    }
    for(long long int i=p;i<=q;i++)
    {
        if(d[l][i]=='-')
            d[l][i]='+';
        else
            d[l][i]='-';
    }
}

int main()
{
    FILE *f,*fp;
    long long int n,i=0;
    f=fopen("B-large.in","r");
    fp=fopen("output.txt","w");
    while(!feof(f))
    {
        fscanf(f,"%s",d[i]);
        i++;
    }
    i=0;
    while(d[0][i]!='\0')
    {
        t*=10;
        t+=(d[0][i]-'0');
        i++;
    }
    for(long long int l=1;l<=t;l++)
    {
        long long int flag=0,ans=0;
        while(!flag)
        {
            long long int a=-1,i=strlen(d[l])-1,b=-1;
            for(;i>=0;i--)
            {
                if(d[l][i]=='-')
                {
                    a=i;
                    break;
                }
            }
            {
                for(long long int j=i;j>=0;j--)
                {
                    if(d[l][j]=='+')
                    {
                        b=j;
                        break;
                    }
                }
            }
            if(a==-1)
            {
                flag=1;
                break;
            }
            else if(b==-1)
            {
                ans++;
                flag=1;
                break;
            }
            else
            {
                if(d[l][0]=='+')
                {
                    flip(0,b,l);
                }
                else
                {
                    flip(0,a,l);
                }
                ans++;
            }
        }
        fprintf(fp,"Case #%lld: %lld\n",l,ans);
    }
    return 0;
}
