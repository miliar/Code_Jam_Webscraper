#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <utility>
#include <limits>
#include <cmath>
#include <cstdlib>

using namespace std;

template <typename T>
string v2s(const vector<T>& v)
{
    ostringstream ss;
    for (int i = 0; i < v.size(); ++i) {
        if (i > 0)
            ss << " ";
        ss << v[i];
    }
    return ss.str();
}

template <typename T>
vector<T> s2v(const string& s)
{
    istringstream ss(s);
    vector<T> v;
    T t;
    while (cin >> t)
	v.push_back(t);
    return v;
}

struct input
{
    int r1;
    vector< vector<int> > g1;
    int r2;
    vector< vector<int> > g2;
};

struct output
{
    int c;
};

istream& operator>>(istream& is, input& in)
{
    is >> in.r1;
    in.g1.resize(4);
    for (int i = 0; i < 4; i++) {
        in.g1[i].resize(4);
        for (int j = 0; j < 4; j++) {
            is >> in.g1[i][j];
        }
        sort(in.g1[i].begin(), in.g1[i].end());
    }
    is >> in.r2;
    in.g2.resize(4);
    for (int i = 0; i < 4; i++) {
        in.g2[i].resize(4);
        for (int j = 0; j < 4; j++) {
            is >> in.g2[i][j];
        }
        sort(in.g2[i].begin(), in.g2[i].end());
    }
    
    return is;
}

ostream& operator<<(ostream& os, const output& out)
{
    if (out.c == -1)
        os << "Bad magician!";
    else if (out.c == -2)
        os << "Volunteer cheated!";
    else
        os << out.c;
    
    return os;
}

output solve(input in)
{
    output out;
    
    vector<int> rc(4);
    rc.resize(set_intersection(in.g1[in.r1 - 1].begin(), in.g1[in.r1 - 1].end(),
                               in.g2[in.r2 - 1].begin(), in.g2[in.r2 - 1].end(),
                               rc.begin())
              - rc.begin());
    
    if (rc.size() == 0)
        out.c = -2;
    else if (rc.size() == 1)
        out.c = rc[0];
    else
        out.c = -1;
    
    return out;
}

int main(int argc, char* argv[])
{
    int T;
    cin >> T;

    for (int t = 0; t < T; ++t) {
	input in;
	cin >> in;

	output out = solve(in);

        cout << "Case #" << t + 1 << ": " << out << endl;
    }

    return 0;
}
