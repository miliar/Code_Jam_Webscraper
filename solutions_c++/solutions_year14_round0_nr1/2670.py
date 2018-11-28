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
        int r1;
        in >> r1;
        --r1;

        int s1[16];
        for(int i = 0; i < 16; ++i) {
            in >> s1[i];
        }

        int r2;
        in >> r2;
        --r2;

        int s2[16];
        for(int i = 0; i < 16; ++i) {
            in >> s2[i];
        }

        vector<int> v1, v2;
        for(int i = 0; i < 4; ++i) {
            v1.push_back(s1[i + 4*r1]);
            v2.push_back(s2[i + 4*r2]);
        }

        sort(v1.begin(), v1.end());
        sort(v2.begin(), v2.end());

        vector<int> res;
        set_intersection(v1.begin(), v1.end(), v2.begin(), v2.end(), back_inserter(res));

        out << "Case #" << q << ": ";
        if(res.size() == 1)
            out << res[0];
        else if(res.empty())
            out << "Volunteer cheated!";
        else
            out << "Bad magician!";
        out << endl;
    }

    return 0;
} 