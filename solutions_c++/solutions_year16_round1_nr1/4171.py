#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int x,y,t,i;
    cin >> t ;
    for(x=1;x<=t;x++)
    {
        char str[1002];
        cin >> str ;
        int l=strlen(str);
        deque<char> dq;
        dq.push_back(str[0]);
        for(i=1;i<l;i++)
        {
            if(str[i]>=dq.front())
                dq.push_front(str[i]);
            else
                dq.push_back(str[i]);
        }
        cout << "Case #" << x << ": " ;
        while(!dq.empty())
        {
            cout << dq.front();
            dq.pop_front();
        }
        cout << endl ;
    }
    return 0;
}
