///underSpirit, Jahangirnagar University, Bangladesh.

#include<bits/stdc++.h>
using namespace std;
#define LL long long
#define ULL unsigned long long
#define FOR(i, s, e) for(int i=s;i<e;i++)
#define REV(i, s, e) for(int i=s-1;i>=e;i--)
#define BUG() cout<<"BUG!"<<endl
#define BUG1(x) cout<<"#"<<x<<endl
#define BUG2(x, y) cout<<"#"<<x<<" #"<<y<<endl
#define READ() freopen("Input.txt", "r", stdin)
#define WRITE() freopen("Output.txt", "w", stdout)

template <typename T>string NumberToString ( T Number ) {/// NumberToString ( Number )
    ostringstream ss;
    ss << Number;
    return ss.str();
}
template <typename T> T StringToNumber ( const string &Text ) {/// StringToNumber <Type> ( String )
    istringstream ss(Text);
    T result;
    return ss >> result ? result : 0;
}
int CheckBigNum(string x, string y) {/// 0 -> (y = x), -1 -> (x < y), 1 -> (x > y)
    int i = 0, j = 0;
    while(x[i] == '0') {
        i++;
    }
    while(y[j] == '0') {
        j++;
    }
    if(x.size() - i > y.size() - j) return 1;
    else if(x.size() - i < y.size() - j) return -1;
    for(;;) {
        if(i == x.size() && j == y.size()) return 0;
        if(x[i] > y[j]) return 1;
        else if(x[i] < y[j]) return -1;
        else i++, j++;
    }
}
int rectInsect(int x1, int y1, int x2, int y2, int x3, int y3, int x4, int y4) {
    int x5 = max(x1, x3);
    int y5 = max(y1, y3);
    int x6 = min(x2, x4);
    int y6 = min(y2, y4);
    if(x5 < x6 && y5 < y6) return (x6 - x5) * (y6 - y5);
    return 0;
}
//______________________________________________________________________________

int main() {
    READ();
    WRITE();
    int tc, cs = 0;
    int i, j, k;
    cin >> tc;
    FOR(cs, 1, tc + 1) {
        int x, y;
        cin >> x;
        x--;
        vector<int>u, v;
        FOR(i, 0, 4) {
            FOR(j, 0, 4) {
                int a;
                cin >> a;
                if(i == x) u.push_back(a);
            }
        }
        cin >> y;
        y--;
        FOR(i, 0, 4) {
            FOR(j, 0, 4) {
                int a;
                cin >> a;
                if(i == y) v.push_back(a);
            }
        }
        vector<int>A;
        FOR(i, 0, 4) {
            FOR(j, 0, 4) {
                if(u[i] == v[j]) {
                    A.push_back(u[i]);
                }
            }
        }
        cout << "Case #" << cs << ": ";
        if(A.size() == 1) cout << A[0] << endl;
        else if(A.size() > 1) cout << "Bad magician!" << endl;
        else cout << "Volunteer cheated!" << endl;
    }
    return 0;
}
/*





*/

