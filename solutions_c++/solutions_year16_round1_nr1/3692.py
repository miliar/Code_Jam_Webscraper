#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("A.in","r",stdin);
    freopen("output.in","w",stdout);
    string s;
    list<char> s1;
    list<char>::iterator it;
    int t;
    char c;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        cin>>s;
        c=s[0];
        s1.push_back(s[0]);
        for(int j=1;j<s.length();j++)
        {
            if((int)s[j]>=(int)c) {s1.push_front(s[j]);c=s[j];}
            else
                {s1.push_back(s[j]);}

        }
        cout<<"Case #"<<i<<": ";
        for(it=s1.begin();it!=s1.end();++it)
        {
            cout<<*it;
        }
        cout<<"\n";
        s1.erase(s1.begin(),s1.end());
    }
    return 0;
}
