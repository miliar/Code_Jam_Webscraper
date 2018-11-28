#include<bits/stdc++.h>
# include<string.h>
using namespace std;
# define ll long long int
void flip(ll n,char a[])
{
    ll i,temp;
    for(i=0;i<=n;i++)
    {
        if(a[i]=='+')
        {
            a[i]='-';
        }
        else
        {
            a[i]='+';
        }
    }

}
bool check(char a[])
{
    ll i,f=1;
    for(i=0;a[i]!='\0';i++)
    {
        if(a[i]=='-')
        {
            f=0;
            break;
        }
    }
    return f;
}
int main()
{

    freopen("B-large.in","r",stdin);
    freopen("output.out","w",stdout);
    ll t,m=0;
    cin>>t;
    for(m=1;m<=t;m++)
    {
            char s[100006];
            cin>>s;

            ll i,j,k=0,count=0,len;
            len=strlen(s);
             while(check(s)!=1)
             {
                 if(s[0]=='+')
                 {
                     for(j=0;s[j]!='\0';j++)
                     {
                         if(s[j]=='-')
                         {
                             flip(j-1,s);
                             count+=1;
                             for(k=0;s[k]!='\0';k++)
                             {
                                 if(s[k]=='+')
                                 {
                                   flip(k-1,s);
                                   count+=1;
                                   break;
                                 }
                             }
                             break;
                         }
                         else if(j==len-1)
                         {
                             break;
                         }
                     }
                 }
                 else if(s[0]=='-')
                 {
                     for(j=0;s[j]!='\0';j++)
                     {
                         if(s[j]=='+')
                         {
                             flip(j-1,s);
                             count+=1;
                             break;
                         }
                         else if(j==len-1)
                         {
                             flip(j,s);
                             count+=1;
                             break;
                         }
                     }
                 }
             }

            cout<<"Case #"<<m<<": "<<count<<endl;
               }
    return 0;
}
