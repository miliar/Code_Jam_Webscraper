#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t;
    cin>>t;
    for(int a=1;a<=t;a++)
    {
        int cnt=0;
        int i;
        string s1;
        cin>>s1;
        int n=(int)s1.size();
        for(i=1;i<n;i++)
        {
            if(s1[i]!=s1[i-1])
            { cnt++;
              int b=i;
              for(int j=0;j<b;j++)
              {
                  s1[j]=s1[i];
              }

            }
        }
        if(s1[n-1]=='-')
            {cnt+=1;}
            cout<<"Case #"<<a<<": "<<cnt<<endl;
    }

    return 0;
}
