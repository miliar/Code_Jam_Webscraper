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
    int P;
    int Q;
};

struct output
{
    int G = 0;
};

struct scratch
{
};

struct memKey
{
    input in;
};

struct memVal
{
    output out;
};

map<memKey, memVal> MEMORY;

istream& operator>>(istream& is, input& in)
{
    is >> in.P;
    char slash;
    is.get(slash);
    is >> in.Q;
    
    return is;
}

ostream& operator<<(ostream& os, const output& out)
{
    if (out.G < 0)
        os << "impossible";
    else
        os << out.G;
    
    return os;
}

output solve(input in, scratch sc)
{
    output out;

    if (in.Q == 1)
        return out;

    int q = in.Q;
//    cerr << q << endl;
    while (q % 2 == 0) {
        q /= 2;
//        cerr << q << endl;
    }
    if (q != 1) {
        out.G = -1;
        return out;
    }
        
    while (in.P < in.Q) {
        in.P *= 2;
        out.G++;
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
	
	scratch sc;

	output out = solve(in, sc);

        cout << "Case #" << t + 1 << ": " << out << endl;
    }

    return 0;
}
