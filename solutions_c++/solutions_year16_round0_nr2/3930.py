#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    cin>>t;
    string s;
    int l;
    int i,c;
    int flips;
    for(c=1;c<=t;c++)
    {
        flips=0;
        cout<<"Case #"<<c<<": ";
        cin>>s;
        s=s+"+";
        l=s.length();

        for(i=1;i<l;i++)
        {
            if(s[i]!=s[i-1])
                flips++;
        }
        cout<<flips<<endl;
    }
}
