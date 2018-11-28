
#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char *argv[])
{
    int t;

    cin >> t;
    for (int prob=0; prob<t; ++prob) {
        int n;
        int m;
        vector<int> v;
        vector<bool> b;
        cin >> n >> m;

        for (int y=0; y<n; ++y) {
            for (int x=0; x<m; ++x) {
                int i;
                cin >> i;

                v.push_back(i);
                b.push_back(false);
            }
        }

        for (int y=0; y<n; ++y) {
            int max = v[y*m];
            int maxx = 0;

            for (int x=1; x<m; ++x) {
                if (v[y*m + x] > max) {
                    max = v[y*m + x];
                    maxx = x;
                }
            }

            for (int x=0; x<m; ++x) {
                if (v[y*m + x] == max) {
                    b[y*m + x] = true;
                }
            }
        }

        for (int x=0; x<m; ++x) {
            int max = v[x];
            int maxy;

            for (int y=0; y<n; ++y) {
                if (v[y*m + x] > max) {
                    max = v[y*m + x];
                    maxy = y;
                }
            }

            for (int y=0; y<n; ++y) {
                if (v[y*m + x] == max) {
                    b[y*m + x] = true;
                }
            }
        }

        bool result = true;

        for (int y=0; y<n; ++y) {
            for (int x=0; x<m; ++x) {
                result = result && b[y*m + x];
            }
        }

        cout << "Case #" << (prob+1) << ": ";
        if (result)
            cout << "YES\n";
        else
            cout << "NO\n";
    }
    return 0;
}
