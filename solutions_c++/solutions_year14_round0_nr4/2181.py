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
    map<double, bool> M;
    map<double, bool> K;
};

struct output
{
    int DW;
    int W;
};

istream& operator>>(istream& is, input& in)
{
    is >> in.N;
    for (int i = 0; i < in.N; i++) {
        double m;
        is >> m;
        in.M[m] = false;
    }
    for (int i = 0; i < in.N; i++) {
        double k;
        is >> k;
        in.K[k] = false;
    }
    
    return is;
}

ostream& operator<<(ostream& os, const output& out)
{
    os << out.DW << " " << out.W;
    
    return os;
}

output solve(input in)
{
    output out;

    out.DW = 0;
    for (auto mt = in.M.begin(); mt != in.M.end(); mt++) {
        auto kt_max = find_if(in.K.rbegin(), in.K.rend(), [mt](decltype(*mt) it) { return !it.second; });
        auto kt_min = find_if(in.K.begin(), in.K.end(), [mt](decltype(*mt) it) { return !it.second; });
        
        mt->second = true;

        if (kt_min->first > mt->first) {
            kt_max->second = true;
        }
        else {
            out.DW++;
            kt_min->second = true;
        }
    }
    
    for (auto mt = in.M.begin(); mt != in.M.end(); mt++)
        mt->second = false;
    for (auto kt = in.K.begin(); kt != in.K.end(); kt++)
        kt->second = false;
    
    out.W = 0;
    for (auto mt = in.M.rbegin(); mt != in.M.rend(); mt++) {
        auto kt_win = find_if(in.K.begin(), in.K.end(), [mt](decltype(*mt) it) { return !it.second && it.first > mt->first; });
        auto kt_lose = find_if(in.K.begin(), in.K.end(), [mt](decltype(*mt) it) { return !it.second; });
        
        mt->second = true;
        
        if (kt_win == in.K.end()) {
            out.W++;
            kt_lose->second = true;
        }
        else {
            kt_win->second = true;
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
