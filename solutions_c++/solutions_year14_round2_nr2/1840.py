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
    freopen("E:\\ACM\\Google Code Jam 2014\\B.in", "r", stdin);
    freopen("E:\\ACM\\Google Code Jam 2014\\outB.txt", "w", stdout);
    #endif // OSW
    ios::sync_with_stdio(false);

    int T;
    cin >> T;
    int t=0;
    while (T-(t++)) {
        int A,B,K;
        cin >> A >> B >> K;
        int sum = 0;
        for (int i=0; i<A; ++i) {
            for (int j=0; j<B; ++j) {
                if ((i&j)<K) ++sum;
            }
        }

        cout << "Case #" << t << ": " << sum << endl;

    }
}


