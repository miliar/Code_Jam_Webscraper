#include <iostream>
#include <map>
#include <cstdio>

using namespace std;

int main()
{
    int t;
    freopen("input1.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin >> t;
    int ans, cs;
    cs = 0;
    while(t--) {
        int n;
        cs++;
        cin >> n;
        map<int, int> mm;
        int val;
        for(int  i = 0; i < 4; i++) {
            for(int j = 0; j < 4; j++) {
                cin >> val;
                if(i+1 == n) {
                    mm[val]++;
                }
            }
        }
        cin >> n;
        int flag;
        flag = 0;
        for(int i = 0; i < 4; i++) {
            for(int j = 0; j < 4; j++) {
                cin >> val;
                if(i+1 == n) {
                    if(mm[val]) {
//cout << "Heelo " << val << endl;
                            flag++;
                            ans = val;
                    }
                }
            }
        }

        cout << "Case #" << cs << ": ";
        if(!flag) {
            cout << "Volunteer cheated!" << endl;
        }
        else if(flag == 1) {
            cout << ans << endl;
        }
        else {
            cout << "Bad magician!" << endl;
        }
    }
}
