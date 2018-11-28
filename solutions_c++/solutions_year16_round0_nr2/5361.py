#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    int i=0;
    while(t--)
    {
        i++;
        string s;
        cin>>s;
        int count1=0;
int         l=s.length();
        if(s[l-1]=='-')
            count1++;
        for(int i=l-1;i>=1;i--)
        {
            if(s[i]!=s[i-1])
                count1++;
        }

    cout<<"Case #"<<i<<": "<<count1<<"\n";
}
}
