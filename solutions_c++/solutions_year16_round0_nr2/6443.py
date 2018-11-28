#include <iostream>

using namespace std;

#include <stdio.h>
#include <stdlib.h>

int length(char *s)
{
    int i=0,c=0;
    while(s[i++]!='\0')
    {
        c++;
    }
    return c;

}
char * getline(char s[])
{
    char c;int i=0;
    while((c=getchar())!='\n')
    {
        s[i++]=c;
    }
    s[i]='\0';
    return s;
}
int main()
{
    freopen ("a.txt","r",stdin);
    freopen ("ao.txt","w",stdout);
    int test,j;
    scanf("%d",&test);
    for(j=0;j<test;j++)
    {
        char str[105];
        cin>>str;
        int l=length(str);char prev='+';int res=0;
        for(int i=l-1;i>=0;i--)
        {
            if(str[i]=='-' && prev=='+')
            {
                res+=1;
                prev='-';
            }
            else if(str[i]=='-' && prev=='-')
            {

                prev='-';
            }
            else if(str[i]=='+' && prev=='-')
            {
                res+=1;
                prev='+';
            }
            else if(str[i]=='+' && prev=='+')
            {

                prev='+';
            }
        }

        printf("Case #%d: ",j+1);
        cout<<res;
        printf("\n");
    }
    return 0;
}
