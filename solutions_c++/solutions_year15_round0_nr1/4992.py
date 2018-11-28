#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    freopen("A-large.in","r",stdin);
    freopen("answer.out","w",stdout);
    int cases; cin>>cases;
    for (int x = 0; x < cases; x++){
        int Smax; string data; cin>>Smax>>data;
        int clapping = 0, friends = 0;
        for (int y = 0; y <= Smax+1; y++){
            while (clapping < y) {
                clapping += 1;
                friends += 1;
            }
            clapping += data[y]-'0';
        }
        cout<<"Case #"<<x+1<<": "<<friends<<endl;
    }
    return 0;
}