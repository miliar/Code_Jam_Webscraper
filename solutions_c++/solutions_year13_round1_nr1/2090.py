#include<iostream>
#include<stdlib.h>
#include<math.h>
#define fileread freopen("/Users/satanforever/Downloads/A-small-attempt0.in.txt","r",stdin)
#define filewrite freopen("/Users/satanforever/gcj/1a/A-small.out","w",stdout)
#define closeread fclose(stdin)
#define closewrite fclose(stdout)
using namespace std;
long double r, t;
int main() {
//fileread;
filewrite;
    int T;
    cin >> T;
    for (int tt = 1; tt <= T; tt++) {
        cout << "Case #" << tt << ": ";
        cin >> r >> t;
        cout << (int)(((1 - 2 * r) + sqrt((2 * r - 1) * (2 * r - 1) + 8 * t)) / 4) << endl;
    }
//closeread;
closewrite;
    return 0;
}
