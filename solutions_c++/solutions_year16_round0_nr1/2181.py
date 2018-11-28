#include<bits/stdc++.h>
using namespace std;
# define ll long long
int main()
{
    ifstream cin("a.txt");
    ofstream cout("b.txt");
    int t,tc=0;
    ll n;
    cin>>t;
    while(t--)
    {
        tc++;
        cout<<"Case #"<<tc<<": ";
        cin>>n;
        set <int> st;
        bool cond=false;
        ll var=1,temp=0,tmp;
        while(st.size()!=10)
        {
            temp+=n;
            tmp=temp;
            while(tmp)
            st.insert(tmp%10),tmp/=10;
            var++;
            if(var==5e4 && st.size()<10)
            {
                cout<<"INSOMNIA\n";
                cond=true;
                break;
            }
        }
        if(!cond)
        cout<<temp<<'\n';
    }
}
