#include<iostream>
using namespace std;

int main () {
    int T;
    cin>>T;

    for(int tt = 1; tt<=T; tt++) {
        int m;
        cin>>m;

        char x;
        int l = 0;
        int how_many = 0;

        cin>>x;
        l+= (x-48);

        for(int i=1; i<=m; i++)
        {
            cin>>x;
            if(i > l) {
                how_many += i - l;
                l = i;
            }
            l+= (x-48);
        }
        cout<<"Case #"<<tt<<": "<<how_many<<endl;
    }
    return 0;
}
