#include<bits/stdc++.h>
using namespace std;
char s[105];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("revengepancakes_output.txt","w",stdout);
    int t,i,st=-1,len,sum,ct,nub=1;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%s",s);
        len=strlen(s);
        ct=0;
        st=-1;
        for(i=0;i<len;i++)
        {
            if(s[i]=='-'&&st==-1)
                st=i;
            else if(s[i]=='+'&&st!=-1)
            {
                if(st==0)
                    ct++;
                else
                    ct+=2;
                st=-1;
            }

        }
        if(st!=-1)
        {
            if(st==0)
                ct++;
            else
                ct+=2;
        }
        printf("Case #%d: ",nub++);
        printf("%d\n",ct);
    }
}
