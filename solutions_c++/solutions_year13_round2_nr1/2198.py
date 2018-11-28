#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <limits>
#include <utility>
#include <cmath>
#include <string>

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
    int N;
    vector<int> M;
};

struct output
{
    int y;
};

istream& operator>>(istream& is, input& in)
{
    is >> in.A;
    is >> in.N;
    in.M = vector<int>(in.N);
    for (int i = 0; i < in.N; ++i)
	is >> in.M[i];

    return is;
}

ostream& operator<<(ostream& os, const output& out)
{
    os << out.y;

    return os;
}

output solve(input in, output out)
{
    //cout << in.A << ", " << v2s(in.M) << endl;

    if (in.M.size() == 0) {
	return out;
    }

    if (in.M[0] < in.A) {
	in.A += in.M[0];
	in.M.erase(in.M.begin());
	return solve(in, out);	
    }

    input in1 = in;
    output out1 = out;
    in1.M.erase(in1.M.begin());
    out1.y++;
    out1 = solve(in1, out1);
    
    if (in.A == 1)
	return out1;

    input in2 = in;
    output out2 = out;
    in2.M.push_back(in.A - 1);
    sort(in2.M.begin(), in2.M.end());
    out2.y++;
    out2 = solve(in2, out2);

    if (out1.y < out2.y)
	return out1;
    return out2;
}

int main(int argc, char* argv[])
{
    int T;
    cin >> T;

    for (int t = 0; t < T; ++t) {
	input in;
	cin >> in;
	sort(in.M.begin(), in.M.end());
	
	output out;
	out.y = 0;
	out = solve(in, out);

        cout << "Case #" << t + 1 << ": " << out << endl;
    }

    return 0;
}
