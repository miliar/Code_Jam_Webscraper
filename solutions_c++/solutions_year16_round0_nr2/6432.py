#include<bits/stdc++.h>
using namespace std;
int T;
string now;
int main()
{
    cin >> T ; 
    for(int data=1;data<=T;data++)
    {
        cin>>now;int ans=0;
        for(int i = now.size() - 1 ; i>=0; --i)
        if(now[i]=='-')
        {
            ++ans;
            for(int j=0;j<=i;j++)
            if(now[j]=='-')now[j]='+';
            else now[j]='-';
        }
        cout<<"Case #"<<data<<": "<<ans<<endl;
    }
    return 0;
}
