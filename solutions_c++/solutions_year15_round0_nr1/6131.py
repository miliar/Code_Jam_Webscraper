#include<bits/stdc++.h>
using namespace std;
int main()
{
    ofstream output;
    ifstream input;
    input.open("A-large.in");
    output.open("outp.out");
    int t,l;
    string s;
    input>>t;
    for(int i=1; i<=t; i++)
    {
        int smax,sum=0,ans=0;
        input>>smax>>s;
        l=s.length();
        int a[l+3];
        a[0]=0;
        for(int j=0; j<l; j++)
        {
            sum+=s[j]-'0';
            a[j+1]=sum;
        }
        for(int j=0; j<l; j++)
        {
            //cout<<ans<<" "<<a[j]<<" "<<j<<endl;
            if(ans+a[j]<j)
            {
                ans+=(j-a[j]-ans);
            }
        }
        output<<"Case #"<<i<<":"<<" "<<ans<<endl;
    }
    input.close();
    output.close();
}
