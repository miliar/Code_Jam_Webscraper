#include <fstream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

typedef long long ll;

const int max_size = 800;

int main()
{
    ofstream out("D:\\output.txt");
    ifstream in("D:\\input.txt");

    int t;
    in >> t;

    for(int q = 1; q <= t; ++q) {
        int n, cap;
        in >> n >> cap;

        vector<int> s(max_size, 0);
        for(int i = 0; i < n; ++i) {
            int x;
            in >> x;
            ++s[x];
        }

        int ans = 0;
        for(int i = 1; i < max_size; ++i) {
            while(s[i]) {
                bool found_pair = false;
                for(int k = max_size-1; k > 0; --k) {
                    if((k != i && s[k] && (k+i <= cap)) || (k == i && s[k] >= 2 && 2*k <= cap)) {
                        ++ans;
                        --s[i];
                        --s[k];
                        found_pair = true;
                        break;
                    }
                }

                if(!found_pair) {
                    ++ans;
                    --s[i];
                }
            }
        }

        out << "Case #" << q << ": " << ans << endl;
    }

    return 0;
}