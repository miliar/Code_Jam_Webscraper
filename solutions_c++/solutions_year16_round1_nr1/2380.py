#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("A-large (4).in","r",stdin);
    freopen("ora.txt","w",stdout);
    int t,z;
    cin>>t;
    for(z=1;z<=t;z++)
    {
        string s;
        cin>>s;
        deque<char> dq;
        int i;
        dq.push_back(s[0]);
        for(i=1;s[i];i++)
        {
            if(s[i]<dq.front())
                dq.push_back(s[i]);
            else dq.push_front(s[i]);
        }
        deque<char>::iterator it;
        cout<<"Case #"<<z<<": ";
        for(it=dq.begin();it!=dq.end();it++)
        {
            cout<<*it;

        }
        cout<<endl;
    }
    return 0;
}
