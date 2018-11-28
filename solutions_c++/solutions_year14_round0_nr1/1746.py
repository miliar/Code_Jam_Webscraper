#include <iostream>
#include <set>
using namespace std;

int main() {
    int T;
    cin>>T;

    for (int i = 1; i <= T; ++i) {
        set<int> s;
        int r, a;
        for (int j = 1; j <= 16; ++j) s.insert(j);
        for (int k = 0; k < 2; ++k) {
            cin>>r;
            for (int row = 0; row < 4; ++row)
                for (int col = 0; col < 4; ++col) {
                    cin>>a;
                    if (row != r-1) s.erase(a);
                }
        }
        if (s.size() == 0) {
            cout<<"Case #"<<i<<": Volunteer cheated!"<<endl;
        } else if (s.size() == 1) {
            cout<<"Case #"<<i<<": "<<(*s.begin())<<endl;
        } else {
            cout<<"Case #"<<i<<": Bad magician!"<<endl;
        }
    }
}
