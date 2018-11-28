#include <iostream>
#include <queue>
#include <cstdio>
using namespace std;
deque <char> q;
string s;
int t,caso,l;
int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    cin>>t;
    for (caso =1; caso<=t;caso++){
        cin>>s;
        l=s.size();
        q.clear();
        q.push_front(s[0]);
        for (int i=1;i<l;i++){
            if (s[i]>=q.front())
                q.push_front(s[i]);
            else
                q.push_back(s[i]);
        }
        cout<<"Case #"<<caso<<": ";
        while (!q.empty()){
            cout<<q.front();
            q.pop_front();
        }
        cout<<endl;
    }
    return 0;
}
