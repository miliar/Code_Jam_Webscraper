#include<bits/stdc++.h>
using namespace std;
string s;
char f(char a)
{
    char x='+',y='-';
    if(a=='+')
        return y;
    else
        return x;
}
void flip(int x)
{
    int i,j=x;
    char a;
    for(i=0;i<j;i++)
    {
        a=s[i];
        s[i]=f(s[j]);
        s[j]=f(a);
        j--;
    }
    if(i==j)
        s[i]=f(s[i]);
}
int main()
{
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);
   int t,x;
   scanf("%d",&t);
   for(x=1;x<=t;x++)
   {
     s.clear();
     cin>>s;
     int y=s.length(),i,j,c=0;
     if(y==1)
     {
         if(s[0]=='+')
            cout<<"Case #"<<x<<": 0\n";
         else
            cout<<"Case #"<<x<<": 1\n";
            continue;
     }
     label:
     for(i=y-1;i>=0;i--)
     {
        if(s[i]=='-')
        break;
        y--;
     }
     if(i<0)
     {
      cout<<"Case #"<<x<<": "<<c<<"\n";
      continue;
     }
     if(s[0]=='-')
     {
        flip(i);
        c++;
        goto label;
     }
     else
     {
         int h=0,loc=-1,m=0;
       for(j=0;j<i;j++)
       {
           if(s[j]=='+')
            h++;
           else
           {
             if(h>m)
             {
                loc=j-1;
                m=h;
             }
             h=0;
           }
       }
       if(h>m)
             {
                loc=j-1;
                m=h;
             }
       if(loc==-1)
        cout<<"Case #"<<x<<": "<<c+1<<"\n";
       else
       {
           flip(loc);
           flip(i);
           c+=2;
           goto label;
       }
     }
   }
    return 0;
}
