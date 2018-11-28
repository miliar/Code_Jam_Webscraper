#include<iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
    int T;
    cin>>T;

    for(int tt = 1; tt<=T; tt++) {
        int x, r, c;
        cin>>x>>r>>c;

        if(r > c)
            swap(r, c);

        bool p=true;
        if(r*c % x != 0)
            p = false;
        else
        if( x == 3)
        {
            if( r == 1 )
                p = false;
        }
        else
        if( x == 4)
        {
            if(r < x && c < x)
                p = false;
            if( (r == 2 || r == 1) && c ==4)
                p = false;
        }
        cout<<"Case #"<<tt<<": ";
        if(p)
            cout<<"GABRIEL"<<endl;
        else
            cout<<"RICHARD"<<endl;
    }
    return 0;
}
