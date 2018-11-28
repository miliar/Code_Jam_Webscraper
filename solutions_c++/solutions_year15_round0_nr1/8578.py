#include <iostream>
#include <string>
#include <algorithm>
#define ll long long int

using namespace std;

int toInt(char c) {
    return (int)( c - '0');
}
int main() {
    int T;
    int M;
    string v;

    cin>>T;
    for (int i = 0; i < T; i++) {
        cin>>M>>v;
        int curr_standing = 0;
        int curr_friends = 0;

        curr_standing += toInt(v[0]);

        for (int k = 1; k <= M; k++) {
            //cout<<"\tk "<<k<<": "<<v[k]<<" curr_standing: "<<curr_standing<<" curr_friends: "<<curr_friends<<endl;
            if (k > curr_standing) {
                curr_friends += (k - curr_standing);
                curr_standing = k;
            }
            curr_standing += toInt(v[k]);
        }
        cout<<"Case #"<<(i +1)<<": "<<curr_friends<<endl;
    }
}