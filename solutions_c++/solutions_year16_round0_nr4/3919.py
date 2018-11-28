#include <iostream>

using namespace std;

int main()
{
    int t; cin>>t;
    int i = 1;
    while(t--) {
        int k, c, s;
        cin>>k>>c>>s;
        cout << "Case #"<<i<<": ";
        if (c==1) {
            for (int j = 1; j<=k; ++j)
                cout << j << " " ;
        }
        else {
            if (k==1)
                cout << 1;
            else {
            for (int j =2; j <= k; ++j)
                cout << j << " ";
            }
        }
        cout <<endl;
        i++;
    }
    return 0;
}
