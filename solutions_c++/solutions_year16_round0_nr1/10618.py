#include <iostream>
#include <map>
#include <iomanip>
#include <algorithm>
#include <set>
#include <complex>
#include <bitset>
using namespace std;

int main() {
    int x,n,res=0;
    freopen("A-large.in", "rt", stdin);
    freopen("out.txt", "wt", stdout);
    cin>>x;
    for (int i = 0; i < x; ++i) {
        cin >> n;
        if (n == 0)
            cout<< "Case #"<<(i+1)<<":"<< " " << "INSOMNIA" << endl;
        else {
            set<int> digits;
            for (int j = 0; j <= 100; ++j) {
                res = j * n;
                while (res) {
                    int digit = res % 10;
                    res /= 10;
                    digits.insert(digit);
                }
                if (digits.size() == 10) {
                    cout << "Case #"<<(i+1)<<":" << " " << (j * n) << endl;
                    break;
                }
            }
        }
    }
    return 0;
}