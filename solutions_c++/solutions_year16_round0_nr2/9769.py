#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t,m=1;
    cin>>t;
    while(t--)
          {
              string s;
              cin>>s;
              int d=0;
                int k=s.length();
    int i=0;

        for(int j=1;j<k;j++)
        { if(i<k-1)
            if(s[i]!=s[j])
            {

                s[i]=s[j];
                d++;
            }

            for(int q=i;q>0;q--)
            {
                s[q]=s[j];
                d++;
            }

            }
            i++;


          if(s[k-1]=='-')
            d++;
          cout<<"Case #"<<m<<": "<<d<<'\n';
m++;
}
return 0;
}
