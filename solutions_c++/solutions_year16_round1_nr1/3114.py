#include <iostream>
#include <algorithm>
#include <list>

using namespace std;

int main() {
    int cases;
    cin>>cases;
    string s;
    for(int k = 0; k < cases; k++) {
        cin>>s;
        list<char> l;
        l.push_front(s[0]);
        for(int i = 1; i < s.size(); i++) {
            if(*l.begin() <= s[i])
                l.push_front(s[i]);
            else
                l.push_back(s[i]);
        }
        cout<<"Case #"<<k+1<<": ";
        list<char>::iterator it = l.begin();
        for( ; it != l.end(); it++){
            cout<<*it;
        }
        cout<<endl;
    }

    return 0;
}
