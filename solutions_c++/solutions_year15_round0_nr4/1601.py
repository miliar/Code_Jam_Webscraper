#include <iostream>
using namespace std;
int main() {
    int t;
    cin>>t;
    for(int xx = 1; xx <= t; ++xx) {
        cout<<"Case #"<<xx<<": ";
        int x,r,c;
        cin>>x>>r>>c;
        if(x == 1) {
            cout<<"GABRIEL\n";
            continue;
        }
        if(x == 2) {
            if((r*c) % 2 == 0) {
                cout<<"GABRIEL\n";
            }
            else cout<<"RICHARD\n";
            continue;
        }
        if(x == 3) {
            if(r < 3 && c < 3) {
                cout<<"RICHARD\n";
                continue;
            }
            if((r*c)%3 != 0) {
                cout<<"RICHARD\n";
                continue;
            }
            if(r*c == 3) {
                cout<<"RICHARD\n";
                continue;
            }
            cout<<"GABRIEL\n";
        }
        if(x == 4) {
            if(r < 4 && c < 4) {
                cout<<"RICHARD\n";
                continue;
            }
            if(r < c) swap(r, c);
            if(r*c == 4) {
                cout<<"RICHARD\n";
                continue;
            }
            if(c == 2) {
                cout<<"RICHARD\n";
                continue;
            }
            cout<<"GABRIEL\n";

        }
    }
}
