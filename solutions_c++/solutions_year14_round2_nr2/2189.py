#include <iostream>
#include <sstream>
#include <iomanip>
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
    int A;
    int B;
    int K;
};

struct output
{
    int P;
};

istream& operator>>(istream& is, input& in)
{
    is >> in.A >> in.B >> in.K;
    return is;
}

ostream& operator<<(ostream& os, const output& out)
{
    os << out.P;
    return os;
}

output solve(input in)
{    
    output out;
    
    out.P = 0;
    for (int a = 0; a < in.A; a++) {
        for (int b = 0; b < in.B; b++) {
            if ((a & b) < in.K)
                out.P++;
        }
    }

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
