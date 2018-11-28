#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("E:/B-large.in","r",stdin);
    freopen("E:/output.txt","w",stdout);
    int t;
    cin>>t;
    int k=0;
    while(t--)
    {

        k++;
        string s;
        cin>>s;
        int sum=0;
        if(s[s.size()-1]=='-')
        {
            sum++;
        }
        for(int i=1;i<s.size();i++)
        {
            if(s[i]!=s[i-1])
                sum++;
        }
        cout<<"Case #"<<k<<": "<<sum<<"\n";
    }

}
