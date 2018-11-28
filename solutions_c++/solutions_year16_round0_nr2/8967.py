#include <bits/stdc++.h>
using namespace std;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int i,j,k,t,m,l;
    char a[105];
    scanf("%d",&t);
    for(l=1;l<=t;l++)
    {
        scanf(" %s",a);
        k=strlen(a);
        m=0;
        if(k==1)
        {
            if(a[0]=='-')
            {
                m=1;
            }
        }
        else
            if(k==2)
            {
                if(a[0]=='+'&&a[1]=='-') m=2;
                if(a[0]=='-'&&a[1]=='+') m=1;
                if(a[0]=='-'&&a[1]=='-') m=1;

            }
        else
        {
            j=0;
            char c=a[0];
            for(i=1;i<k;i++)
            {
                if(c!=a[i])
                {
                    j=1;
                    break;
                }
            }
            if(j==0)
            {
                if(c=='-')
                {
                    m=1;
                }
            }
            if(j==1){
                    j=0;
            for(i=0;i<k-1;i++)
            {
                if(a[i]!=a[i+1])
                {
                    j=1;
                    m++;
                }
            }
            if(j==1) m++;
            //printf("%d\n",m);
            if(m%2!=0&&a[0]=='+'&&a[k-1]=='+') m--;
            if(a[0]=='-'&&a[k-1]=='+') m--;
            }
      }
        //printf("%s\n",a);
        printf("Case #%d: %d\n",l,m);
    }
    return 0;
}
