#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
    freopen ("C:\\Users\\Ganeshraj\\Desktop\\A-large.in","r",stdin);
    freopen ("C:\\Users\\Ganeshraj\\Desktop\\myfile.txt","w",stdout);
    int r,i,t,n,m,tt=1;
    char str[10000];
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d %s\n",&n,str);
        m=r=0;
        for(i=0;i<=n;i++)
        {
            if(m<i)
                {
                    r+=(i-m);
                    m+=(i-m);
                }
            m+=(str[i]-'0');
        }
        printf("Case #%d: %d\n",tt,r);
        tt++;
    }
  //printf ("This sentence is redirected to a file.");
    fclose (stdout);
    fclose (stdin);
    return 0;
}
