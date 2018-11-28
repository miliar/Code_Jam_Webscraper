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
    int N;
    vector<string> lines;
    
};

struct output
{
    int m = 0;
};

struct scratch
{
    char last = 0;
    int m = 0;
};

istream& operator>>(istream& is, input& in)
{
    is >> in.N;
    in.lines.resize(in.N);
    for (int n = 0; n < in.N; n++)
        is >> in.lines[n];
    
    return is;
}

ostream& operator<<(ostream& os, const output& out)
{
    if (out.m < 0)
        os << "Fegla Won";
    else
        os << out.m;
    
    return os;
}

output solve(input in, scratch sc)
{
    output out;
    
    if (in.lines[0].size() == 0 && in.lines[1].size() == 0) {
        out.m = sc.m;
        return out;
    }
    
    if (in.lines[0].size() == 0) {
        if (sc.last == in.lines[1][0]) {
            sc.m++;
            in.lines[0] = string(1, sc.last);
            return solve(in, sc);
        }
        out.m = -1;
        return out;
    }
    
    if (in.lines[1].size() == 0) {
        if (sc.last == in.lines[0][0]) {
            sc.m++;
            in.lines[1] = string(1, sc.last);
            return solve(in, sc);
        }
        out.m = -1;
        return out;
    }
    
    if (in.lines[0][0] == in.lines[1][0]) {
        sc.last = in.lines[0][0];
        in.lines[0] = in.lines[0].substr(1);
        in.lines[1] = in.lines[1].substr(1);
        return solve(in, sc);
    }

    if (sc.last == 0) {
        out.m = -1;
        return out;        
    }
    
    if (sc.last == in.lines[0][0]) {
        scratch sc1 = sc;
        sc1.m++;
        input in1 = in;
        in1.lines[1] = string(1, sc1.last) + in1.lines[1];
        return solve(in1, sc1);
    }
    if (sc.last == in.lines[1][0]) {
        scratch sc1 = sc;
        sc1.m++;
        input in1 = in;
        in1.lines[0] = string(1, sc1.last) + in1.lines[0];
        return solve(in1, sc1);
    }

    out.m = -1;
    return out;
}

int main(int argc, char* argv[])
{
    int T;
    cin >> T;

    for (int t = 0; t < T; ++t) {
	input in;
	cin >> in;
	
	scratch sc;

	output out = solve(in, sc);

        cout << "Case #" << t + 1 << ": " << out << endl;
    }

    return 0;
}
