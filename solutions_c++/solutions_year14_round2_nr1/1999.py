#define OSW2
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <utility>
using namespace std;


string str[105];


int main() {
    #ifdef OSW
    freopen("C:\\Users\\Oswww\\Desktop\\in.txt", "r", stdin);
    #endif // OSW
    #ifdef OSW2
    freopen("E:\\ACM\\Google Code Jam 2014\\A.in", "r", stdin);
    freopen("E:\\ACM\\Google Code Jam 2014\\outA.txt", "w", stdout);
    #endif // OSW
    ios::sync_with_stdio(false);

    int T;
    cin >> T;
    int t=0;
    while (T-(t++)) {
        int n;
        cin >> n;
        for (int i=0; i!=n; ++i) cin >> str[i];
        //for (int i=0; i!=n; ++i) cout << str[i] << endl;

        bool flag = false;
        int sum = 0;
        while(str[0].size()) {
            char ch = str[0][0];
            int num[105];
            for (int i=0; i!=n; ++i) {
                int cnt = 0;
                while (cnt!=str[i].size() && str[i][cnt]==ch) ++cnt;
                num[i] = cnt;
                str[i] = str[i].substr(cnt, str[i].size()-cnt);
                if (0==cnt) flag = true;
            }
            if (flag) break;
            int part = 10000000;
            for (int i=0; i!=n; ++i) {
                int cnadidate_part = 0;
                for (int j=0; j!=n; ++j) {
                    cnadidate_part += abs(num[j]-num[i]);
                }
                part = min(part, cnadidate_part);
            }
            //cout << part << ' ';
            sum += part;
        }
        for (int i=0; i!=n; ++i) if(str[i].size()) flag = true;
        //cout << endl;
        cout << "Case #" << t << ": ";
        if (flag) cout << "Fegla Won" << endl;
        else    cout << sum << endl;
    }
}


