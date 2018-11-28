#include <iostream>
#include <algorithm>
#include <cstdio>
#include <deque>
#include <string>


#define rep(i,a,b) for(int i=a;i<b;i++)

using namespace std;

int main() {
    freopen("f1.in","r",stdin);
    freopen("f1.out","w",stdout);
    int T;
    cin>>T;
    rep(t,1,T+1) {
        string str;
        cin>>str;


        deque<char> qu;
        qu.push_back(str[0]);
        rep(i,1,str.size()) {
            if(str[i]>= *(qu.begin())) {
                qu.push_front(str[i]);
            }
            else {
                qu.push_back(str[i]);
            }

        }
        cout<<"Case #"<<t<<": ";
        for(deque<char>::iterator it=qu.begin();it!=qu.end();++it) {
            cout<<*it;
        }
        cout<<endl;



    }


}
