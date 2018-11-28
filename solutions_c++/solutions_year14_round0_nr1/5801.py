#include <iostream>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <map>
#include <fstream>
#include <utility>
#include <cmath>
#include <limits>
#include <set>
#include <iomanip>

#define cin fin
#define cout fout

#define all(c) c.begin(),c.end()
#define traverse(c,it) for(typeof(c.begin()) it = c.begin(); it != c.end(); it++)
#define ll long long
#define oo numeric_limits<int>::max();

using namespace std;

ifstream fin ("input.in");
ofstream fout ("output.out");

int main()
{
    int T,a,b;
    int f[4][4];
    int s[4][4];
    cin >> T;
    for(int t=0;t<T;t++){
        bool p[16] = {false};
        cin >> a;
        for(int y=0;y<4;y++) {
            for(int x=0;x<4;x++) {
                cin >> f[x][y];
            }
        }
        for(int x=0;x<4;x++)
            p[f[x][a-1]-1] = true;
        cin >> b;
        for(int y=0;y<4;y++) {
            for(int x=0;x<4;x++) {
                cin >> s[x][y];
            }
        }
        int ok = -1;
        for(int x=0;x<4;x++) {
            if(p[s[x][b-1]-1]) {
                if(ok==-1)
                    ok = s[x][b-1];
                else if(ok!=-1)
                    ok = -2;
            }
        }
        cout << "Case #" << t+1 << ": ";
        if(ok==-1)
            cout << "Volunteer cheated!";
        else if(ok == -2)
            cout << "Bad magician!";
        else
            cout << ok;
        cout << endl;
    }
    return 0;
}
