#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;
int main()
{
    freopen("B-large.in","rt",stdin);
freopen("outputhits.cpp","wt",stdout);
    int t,j=1;
    scanf("%d",&t);
    while(t--)
    {
        char s[105]={0};
cin>>s;        int i=0,count=0,k=0;
        int l=strlen(s);
        while(s[i]=='-')
        {
            i++;
            k=1;

        }
        if(s[0]=='-')
            {
                count++;
//printf("%d\n",count);
            }
            while(s[i]=='+')
                    i++;

        for(;s[i]!='\0';i++)
        {
            int f=0;
            while(s[i]=='-')
                  {
                      i++;
                      f=1;
                      k=1;
                  }
                  if(f)
                  count+=2;
                 // printf("%d\n",count);
            //printf("%c\n",s[i]);
        }
        //if(s[0]=='+'&&s[l-1]=='+'&&k==1)
         //   count++;
        printf("Case #%d: %d\n",j++,count);
       // printf("%s\n",s);
    }
    return 0;
}
