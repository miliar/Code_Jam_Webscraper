#include<iostream>
#include<deque>
using namespace std;


int main() {
    ios_base::sync_with_stdio(0);
    int T;
    cin>>T;
    for(int tt=1; tt<=T; tt++) {
        cout<<"Case #"<<tt<<": ";
        string S;
        cin>>S;
        deque<char> D;
        D.push_front(S[0]);
        for(int i=1; i<S.length(); i++) {
            if(D.front() > S[i])
                D.push_back(S[i]);
            else
                D.push_front(S[i]);
        }
        for(int i=0; i<D.size(); i++)
            cout<<D[i];
        cout<<endl;
    }
    return 0;
}
