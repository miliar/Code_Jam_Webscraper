#include <bits/stdc++.h>

using namespace std;

char c[10005];

int main()
{
    int t,sum,i,x,k,j;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        sum=0;
        cin>>x;
        cin>>c;
        if(c[0]=='0')
            {
                sum=1;
                k=1;
            }
        else
           {
               sum=0;
               k=c[0]-'0';
           }
        for(j=1;j<strlen(c);j++)
        {
            if(c[j]=='0')
            {
              if(k<j)
              {
                  sum+=(j-k);
                  k+=(j-k);
              }
            }
             else
             {
              if(k<j)
              {
                  sum+=(j-k);
                  k+=(j-k);
              }
                    k+=c[j]-'0';
             }
        }
        cout<<"Case #"<<i<<": "<<sum<<endl;
    }
}
