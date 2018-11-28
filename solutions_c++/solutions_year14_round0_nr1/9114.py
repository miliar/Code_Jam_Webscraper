#include <iostream>
#include <cstring>
using namespace std;
int main() {
    int t;
    cin>>t;
    for (int ncase = 1; ncase <= t; ncase++) {
        int tmp;
        int firAns[4];
        int firstAns, secondAns;
        cin>>firstAns;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                cin>>tmp;
                if (i + 1 == firstAns) {
                    firAns[j] = tmp;
                }
            }
        }
        cin>>secondAns;
        int matched = 0;
        int matval = 0;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                cin>>tmp;
                if (i + 1 == secondAns) {
                    for (int k = 0; k < 4; k++) {
                        if (firAns[k] == tmp) {
                            matched++;
                            matval = tmp;
                        }
                    }
                }
            }
        }
        cout<<"Case #"<<ncase<<": ";
        switch (matched) {
            case 0:
                cout<<"Volunteer cheated!"<<endl;
                break;
            case 1:
                cout<<matval<<endl;
                break;
            default:
                cout<<"Bad magician!"<<endl;
                break;
        }
    }
    return 0;
}
