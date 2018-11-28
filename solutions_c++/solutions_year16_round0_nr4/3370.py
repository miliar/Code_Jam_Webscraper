#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("4.out","w",stdout);
	freopen("4.in","r",stdin);
	int t;
	cin>>t;
    for(int _=0;_<t;_++)
    {
        int k,c,s;
        cin>>k>>c>>s;
        cout<<"Case #"<<_+1<<": ";
        if(c==1 || k==1)
        {
            if(k>s)
                cout<<"IMPOSSIBLE"<<endl;
            else
                for(int i=0;i<k;i++)
                    cout<<i+1<<(i<k-1?" ":"\n");
        }
        else if(k-1>s)
            cout<<"IMPOSSIBLE"<<endl;
        else
            for(int i=1;i<k;i++)
                cout<<i+1<<(i<k-1?" ":"\n");
    }
    return 0;
}
