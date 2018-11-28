#include<bits/stdc++.h>

using namespace std;

int main() {

    freopen("C:\\Users\\Saurabh\\Desktop\\in.txt","r",stdin);
    freopen("C:\\Users\\Saurabh\\Desktop\\out.txt","w",stdout);
    int t,cas=1;
    cin>>t;
    while(t--) {
        int i;
        deque <char> q;
        string s;
        cin>>s;
        q.push_back(s[0]);
        for(i=1;i<s.size();i++) {
            if(s[i]>=q.front())
                q.push_front(s[i]);
            else
                q.push_back(s[i]);
        }
        cout<<"Case #"<<cas++<<": ";
        for(i=0;i<q.size();i++)
            cout<<q[i];
        cout<<endl;
    }

    return 0;
}
