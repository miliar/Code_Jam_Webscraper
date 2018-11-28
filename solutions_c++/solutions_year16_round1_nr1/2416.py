#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

deque<char>dq;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    string s;
    int t;
    cin>>t;
    int j=1;
    char c;
    while(j<=t)    {
        cin>>s;
        dq.push_back(s[0]);
        c=s[0];
        for(int i=1;i<s.size();i++)    {
            if(s[i]>=c)    {
                dq.push_front(s[i]);
                c=s[i];
            }
            else    dq.push_back(s[i]);
        }
        cout<<"Case #"<<j<<": ";
        for(int i=0;i<dq.size();i++)    {
            cout<<dq[i];
        }
        cout<<endl;
        dq.clear();
        j++;
    }
    return 0;

}
