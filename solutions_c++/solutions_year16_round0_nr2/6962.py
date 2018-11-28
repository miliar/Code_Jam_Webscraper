#include<bits/stdc++.h>
using namespace std;
int main()
{
    ifstream cin("concom.in");
    ofstream cout("concom.out");
    long long i,t,has,cont=0;
    string st;
    char now;
    cin>>t;
    while(t--)
    {
        cout<<"Case #"<<++cont<<": ";
        cin>>st;
        now=st[0];
        has=0;
        for(i=1;i<st.length();++i)
        {
            if(st[i]!=now)
            {
                now=st[i];
                has++;
            }
        }
        if(st[st.length()-1]=='-')
        {
            cout<<has+1<<endl;
        }
        else cout<<has<<endl;
    }
}
