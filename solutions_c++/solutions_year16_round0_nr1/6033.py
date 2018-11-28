#include <iostream>
#include <set>

using namespace std;

typedef long long LL;

int main() {
    set<int> digits;
    int T, n, i;
    LL cv;

    cin>>T;

    int c=1;
    for (; c<=T; ++c) {
        cin>>n;

        digits.clear();
        for ( i=1; i<=101; ++i) {
            cv = n*(LL)i;

            while (cv) {
                digits.emplace(cv % 10);

                if (digits.size() == 10) {
                    break;
                }
                cv /= 10;
            }

            if (cv != 0) {
                break;
            }
        }
        
        cout<<"Case #"<<c<<": ";
        if (i > 101) {
            cout<<"INSOMNIA\n";
        } else {
            cout<<n*(LL)i<<"\n";
        }
        
    }

    return 0;
}

