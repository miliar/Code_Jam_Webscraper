#include <iostream>
#include <string>

int his [3000] = {0};

using namespace std;

int main()
{
    int t, n;
    cin>>t;
    for (int i = 1; i <= t; ++i) {
             cin>>n;
            for (int j = 0; j <= 2500; ++j) {
                his[j] = 0;
            }
        for (int j = 0; j < n*2-1; ++j) {
            for (int k = 0; k < n; ++k) {
                    int x;
                cin>>x;
                ++his[x];
            }
        }
        cout<<"Case #"<<i<<": ";
        for (int j = 1; j <= 2500; ++j) {
            if (his[j]%2 == 1) {
                cout<<j<<" ";
            }
        }

        cout<<endl;
    }

    return 0;
}
