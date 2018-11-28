#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("case.out","w",stdout);
    string r;
    int t,d=0;
    cin>>t;
    int n,k;
    for(int j=1;j<=t;j++)
    {
        cin>>r;
        while(count(r.begin(),r.end(),'+')!=r.length())
        {
            n=r.find('-');
            k=r.find('+',n);
            if(k<0)
            {
                for(int i=0;i<r.length();i++)
            {
                if(r[i]=='+')
                r[i]='-';
                else
                r[i]='+';
            }
            d++;
            }
            if(count(r.begin(),r.end(),'+')!=r.length())
            {
             n=r.find('-');
             k=r.find('+',n);
            for(int i=0;i<k;i++)
            {
                if(r[i]=='+')
                r[i]='-';
                else
                r[i]='+';
            }
             d++;
            }
        }
        cout<<"Case #"<<j<<": "<<d<<"\n";
        d=0;
    }
    return 0;
}
