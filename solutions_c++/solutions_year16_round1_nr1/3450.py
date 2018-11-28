#include<iostream>
#include<string>
#include<deque>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int kase=1;kase<=t;kase++) {
        string s;
        cin>>s;
        deque<char> D;
        for(int i=0;i<(int)s.size();i++) {
            if(D.empty()) {
               D.push_front(s[i]);
               continue;
            }
            if(s[i] >= D.front())
                D.push_front(s[i]);
            else
                D.push_back(s[i]);
        }
        cout<<"Case #"<<kase<<": ";
        for(deque<char>::iterator it = D.begin(); it!=D.end(); ++it) {
            cout<<(*it);
        }
        cout<<endl;
    }
    return 0;
}
