#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("last.out","w",stdout);
    int t;
    cin>>t;
    int j=1;
    while(t--)
{
    string s;
    cin>>s;
    deque<char>d;
    deque<char>::iterator it;
    char large;
    large=s[0];
    d.push_back(s[0]);
    for(int i=1;i<s.length();i++)
    {
        if(s[i]>=large)
        {
            large=s[i];
            d.push_front(s[i]);
        }
        else
            d.push_back(s[i]);
    }
    cout<<"Case #"<<j<<": ";
    for(it=d.begin();it!=d.end();++it)
        cout<<*it;
    cout<<endl;
    j++;
}
    return 0;
}
