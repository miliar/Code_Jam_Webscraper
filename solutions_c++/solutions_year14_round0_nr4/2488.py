#include <vector>
#include <algorithm>
#include <iterator>
#include <iomanip>
#include <fstream>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    
    ifstream in("D:\\input.txt");
    ofstream out("D:\\output.txt");

    int t;
    in >> t;

    out << fixed << setprecision(7);

    for(int q = 1; q <= t; ++q) {
        int n;
        in >> n;

        vector<pair<double, bool> > all(2*n);
        
        for(int i = 0; i < n; ++i) {
            in >> all[i].first;
            all[i].second = true;
        }

        for(int i = 0; i < n; ++i) {
            in >> all[i+n].first;
            all[i+n].second = false;
        }

        sort(all.begin(), all.end());

        vector<bool> done(2*n, false);
        int y = 0;
        int r = 2*n;
        int kens = 0;
        for(int i = 0; i < 2*n; ++i) {
            if(!all[i].second && !done[i]) {
                ++kens;
            }
            if(all[i].second) {
                if(kens) {
                    ++y;
                    --kens;
                } else {
                    --r;
                    while(r >= 0 && all[r].second) {
                        --r;
                    }
                    done[r] = true;
                }
            }
        }

        int z = 0;
        kens = 0;
        for(int i = 2*n-1; i >= 0; --i) {
            if(all[i].second) {
                if(kens) {
                    --kens;
                } else {
                    ++z;
                }
            } else {
                ++kens;
            }
        }

        out << "Case #" << q << ": " << y << " " << z << endl;
    }

    return 0;
} 