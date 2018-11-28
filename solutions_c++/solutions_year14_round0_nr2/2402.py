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
    double C;
    double F;
    double X;
};

struct output
{
    double y;
};

istream& operator>>(istream& is, input& in)
{
    is >> in.C >> in.F >> in.X;
    
    return is;
}

ostream& operator<<(ostream& os, const output& out)
{
    os << fixed << setprecision(7) << out.y;
    
    return os;
}

output solve(input in)
{
    output out;
    
    double Tt = 0;
    double Xt = 0;
    double Rt = 2;
    
    while (true) {
        if (in.X - Xt < in.C) {
            Tt += (in.X - Xt) / Rt;
            break;
        }
        
        double t1 = (in.X - Xt) / Rt;
        double t2 = ((in.X - Xt) / (Rt + in.F)) + (in.C / Rt);

        Tt += (in.C) / Rt;
        
        if (t1 < t2) {
            Xt += in.C;
        }
        else {
            Rt += in.F;
        }
    }
    
    out.y = Tt;
    
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
