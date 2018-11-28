#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
int n;


int main()
{
  freopen("B-large.in","r",stdin);
   freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    for(int j=1; j<=t; j++)
    {
        string s;
        cin>>s;
        n=s.size();
        int pmin=0;
        for(int i=0 ; i <n; i++)
        {
            if(s[i]=='-')
            {
                if(i==0)pmin+=1;
                else
                {
                    if(s[i-1]=='+')pmin+=2;
                }
            }

        }
        cout<<"Case #"<<j<<": "<<pmin<<endl;



    }

    return 0;
}
