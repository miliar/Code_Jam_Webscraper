#include<bits/stdc++.h>
using namespace std;
int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    deque<char> q;
    int t,c=1;
    string s;
    cin>>t;
    while(t--){
        cin>>s;
        int len=s.length();
        q.push_front(s[0]);
        for(int i=1;i<len;i++){
            char x=q.front();
            if(s[i]>=x)
                q.push_front(s[i]);
            else
                q.push_back(s[i]);
        }
        cout<<"Case #"<<c++<<": ";
        for(int i=0;i<len;i++)
        {
            cout<<q.front();
            q.pop_front();
        }
        cout<<"\n";
    }
    return 0;
}
