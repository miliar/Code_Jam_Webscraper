/* coder: Anh Tuan Nguyen */
#include <bits/stdc++.h>
using namespace std;

int main()
{
#ifdef gsdt
    freopen("a-large.in","r",stdin);
    freopen("a.out","w",stdout);
#endif // gsdt

    int T;
    cin>>T;
    for(int qq=1; qq<=T; qq++)
    {
        deque<char> dq;
        string s;
        cin>>s;
        for(int i=0; i<s.length(); i++)
        {
            if(dq.empty()) dq.push_back(s[i]);
            else
            {
                if(dq.front()>s[i]) dq.push_back(s[i]);
                else dq.push_front(s[i]);
            }
        }
        printf("Case #%d: ",qq);
        for(int i=0; i<dq.size(); i++)
            cout<<dq[i];
        cout<<endl;
    }

    return 0;
}

