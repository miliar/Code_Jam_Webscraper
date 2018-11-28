#include<bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{

    freopen("B-large.in","r",stdin);
    freopen("ggBl.out","w",stdout);
     ll i,j,k,l,n,T,t=1,p=0,m=0,c=0;
    string s;
    cin >> T;
    while(T--)
    {
        cin >>s;
        for(i=0;i<s.length();i++)
        {
            if(s[i]=='-')
            {
               m=1;

                if(s[i+1]=='+')
                {
                    c++;
                    p=1;
                    m=0;
                }



            }
            if(s[i]=='+')
            {   p=1;

               // c++;
                  if(s[i+1]=='-')
                  {
                      c++;
                      m=1;
                      p=0;
                  }
            }


        }
        if(m==1)
        {
            c++;
        }
       // Case #1: 1
        cout <<"Case #" <<t <<": " <<c <<endl;
        t++;
        m=0;
        p=0;
        c=0;

    }


    return 0;
}
