#include<bits/stdc++.h>
using namespace std;

int main()
{
      long long int t,count;
      string st;
      int o=0;
      scanf("%lld",&t);
      while(t--)
      {
            o++;
            cin>>st;
            char prev=st[0];
            if(prev=='-')
            count=1;
            else
            count=0;
            int i=0;
            while(st[i]=='-')
            {
                  i++;
            }
            prev=st[i];
            for(;i<st.size();i++)
            {
                  if(st[i]!=prev)
                  {
                        if(prev=='+')
                        count+=2;
                        prev=st[i];
                  }
            }
            printf("Case #%d: %lld\n",o,count);
      }
}