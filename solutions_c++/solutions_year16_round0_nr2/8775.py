#include <bits/stdc++.h>
#include <fstream>

using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t; cin>>t;
    for (int tt=1;tt<=t;tt++)
    {
        string str; cin>>str;
        stack<char>st;
        for (int i=str.size()-1;i>=0;i--) st.push(str[i]);
        if (st.top()=='+')
        {
            int i=0;
            while (!st.empty())
            {
                int c=0;
                //++--++
                while (!st.empty())
                {
                    if (st.top()=='-') break;
                    st.pop();
                    c=1;
                }
                if (c&&!st.empty()) i+=2;
                while (!st.empty())
                {
                    if (st.top()=='+') break;
                    st.pop();
                }
            }
            cout<<"Case #"<<tt<<": "<<i<<endl;
        }
        else
        {
            int i=0;
            while (!st.empty())
            {
                int c=0;
                while (!st.empty())
                {
                    if (st.top()=='+') break;
                    st.pop();
                    c=1;
                }
                if (c) i++;
                c=0;
                while (!st.empty())
                {
                    if (st.top()=='-') break;
                    st.pop();
                    c=1;
                }
                if (c&&!st.empty()) i++;
            }
            cout<<"Case #"<<tt<<": "<<i<<endl;
        }
    }
    return 0;
}
