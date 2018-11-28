#include <iostream>
#include <fstream>

using namespace std;

int main() {
    ifstream cin("input.txt");
    ofstream cout("output.txt");

    int t;
    cin >> t;

    for( int cs = 1; cs <= t; ++cs ) {
        int smax;
        string str;

        cin >> smax >> str;

        int cnt = 0, sz = str.length(), pre = str[0]-'0';
        for( int i = 1; i < sz; ++i ) {
            int b = str[i]-'0';
            if( i <= pre ) {
                pre += b;
            }
            else {
                if( b == 0 ) continue;
                //cout << "i: " << i << " cnt:" << cnt << " pre: " << pre << endl;
                cnt += (i-pre);
                pre += (i-pre)+b;
                //cout << "i: " << i << " cnt:" << cnt << " pre: " << pre << endl;
            }
        }

        cout << "Case #" << cs << ": " << cnt << endl;
    }
}
