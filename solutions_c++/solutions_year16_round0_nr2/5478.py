#include<iostream>
#include<string.h>
using namespace std;
int findLastMinus(char s[])
{
    int n=strlen(s);
    for(int i=n-1;i>-1;i--)
    if(s[i]=='-')
    return i;
    
    return -1;
    
}
void flipTill(int x,char s[])
{
    for(int i=0;i<=x;i++)
    {
        if(s[i]=='-')
        s[i]='+';
        else
        s[i]='-';
    }
    for(int i=0;i<=x/2;i++)
    {
        char temp=s[i];
        s[i]=s[x-i];
        s[x-i]=temp;
    }
}
int findFirstMinus(char s[])
{
    int n=strlen(s);
    for(int i=0;i<n;i++)
    if(s[i]=='-')
    return i;
    
    return -1;
    
}
int main()
{
    int t;
    cin>>t;
    int caseNo=1;
    while(t-->0)
    {
        char s[102];
        cin>>s;
        int c=0;
        int x=findLastMinus(s);
        while(x!=-1)
        {
            if(s[0]=='+')
            {
                //s[0]='-';
                int y;
                y=findFirstMinus(s);
                flipTill(y-1,s);
                //cout<<"y="<<y<<"S="<<s<<endl;
                c++;
            }
            
            flipTill(x,s);
            c++;    
            x=findLastMinus(s);
        }
        cout<<"Case #"<<caseNo<<": "<<c<<endl;
        caseNo++;
    }
    return 0;
}
