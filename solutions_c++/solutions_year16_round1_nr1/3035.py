#include <iostream>
#include <cstdio>
#include <deque>

using namespace std;

deque<char> q;

int main()
{
    freopen("a.txt","r",stdin);
    freopen("b.txt","w",stdout);
    ios_base::sync_with_stdio(false);
    int t;
    cin >> t;
    int x = 1;
    while(t--){
        string s;
        cin >> s;
        int i=0;
        q.clear();
        q.push_back(s[i]);
        i++;
        for(;i<s.length();i++){
            if(s[i]>=q.front())q.push_front(s[i]);
            else q.push_back(s[i]);
        }
        cout << "Case #" << x++ << ": ";
        for(deque<char>::iterator j = q.begin();j!=q.end();j++){
            cout << q.front();
            q.pop_front();
        }
        cout << endl;
    }
    return 0;
}
