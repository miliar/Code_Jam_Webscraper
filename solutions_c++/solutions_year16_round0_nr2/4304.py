#include <iostream>

using namespace std;

int main()
{
    long long t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        string s;
        cin>>s;
        long long int c=0,c1;
        int flag;
        if(s[0]=='+')
        {
            flag=1;
            for(int j=1;j<s.length();j++)
            {
                  if(flag==1 && s[j]=='-')
                  {
                       flag=0;
                       c++;
                  }
                  else if(flag==0 && s[j]=='+')
                  {
                       flag=1;
                  }

            }
            c1=2*c;
        }
        else
        {
            flag=0;
            c=1;
            for(int j=1;j<s.length();j++)
            {
                  if(flag==1 && s[j]=='-')
                  {
                       flag=0;
                       c++;
                  }
                  else if(flag==0 && s[j]=='+')
                  {
                       flag=1;
                  }

            }
            c1=2*c-1;
        }
        cout<<"Case #"<<i<<": "<<c1<<endl;
    }
}
