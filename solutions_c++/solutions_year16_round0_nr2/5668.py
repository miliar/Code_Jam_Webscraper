#include <bits/stdc++.h>
using namespace std;
int main()
    {
    long long int n,i,l,p,m,c,j;char s[10000],si[1000];
    cin>>n;gets(si);
    for(i=0;i<n;i++)
        {
         gets(s);p=0;c=0;m=0;
         l=strlen(s);
         if(s[0]=='+')
             {p=1;m=0;}
         else
             {c++;p=0;m=1;}
        
          for(j=1;j<l;j++)
              {
              if(s[j]=='-'&&p==0)
                  {
                    m=1;p=0;
                  }
               else if(s[j]=='+')
                   {
                    p=1;m=0;
                   }
               else if(s[j]=='-'&&p==1)
                   {
                    p=0;m=1;c+=2;
                   }
              }
          cout<<"Case "<<"#"<<i+1<<": "<<c<<endl;
       }
    return 0;
}