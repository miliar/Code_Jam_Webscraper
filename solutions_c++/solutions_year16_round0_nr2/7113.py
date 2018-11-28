#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    int tc=1;
    while(tc<=t)
    {
        string s;
        cin>>s;
        int n=s.length();
        int k=0;
        int i=0;
        while(i<n)
        {
            int j=i;
            while(s[j]==s[i])
                j++;
            k++;
            i=j;
        }
        if(s[n-1]=='+')
            k--;
        cout<<"Case #"<<tc<<": "<<k<<endl;
        tc++;
    }

return 0;
}
