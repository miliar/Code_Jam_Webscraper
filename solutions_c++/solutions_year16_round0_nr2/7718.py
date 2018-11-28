#include <iostream>
#include<cstring>
using namespace std;
int getlast(char *s)
{
    long long int last,x=0,i;
    for( i=0;i<strlen(s);i++)
    {
        if(s[i]=='-')
        {
            last=i;
        }
        else
        {
           x++; 
        }
    }
    if(x==strlen(s))
    {
        return -1;
    }
    return last;
}
int clean(char *s,int last)
{
    long long int i=0,count=0;
    while(i<=last)
    {
        if(s[i]=='-')
        {
            s[i]='+';
        }
        else
        {
            s[i]='-';
            count++;
        }
        i++;
    }
    return count;
}
int main()
{
    long long int t,i;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        long long int res=0,j,last,count=1;
        char s[12312];
        cin>>s;
        char s1[12312];
        for(j=strlen(s)-1;j>=0;j--)
        {
            s1[j]=s[j];
        }
        while(count)
        {
            long long int last=getlast(s1);
            if(last==-1)
            {
                break;
            }
            count=clean(s1,last);
            res++;
        }
        cout << "Case #" << i << ": " << res << endl;
    }
    return 0;
}
