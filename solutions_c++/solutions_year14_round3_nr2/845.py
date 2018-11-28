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
    vector<string> cars;
};

struct output
{
    int W = 0;
};

struct scratch
{
    int N;
    vector<string> cars;
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
    is >> in.N;
    in.cars.resize(in.N);
    for (int i = 0; i < in.N; i++)
        is >> in.cars[i];
    
    return is;
}

ostream& operator<<(ostream& os, const output& out)
{
    os << out.W;
    
    return os;
}

bool is_valid(const string& train)
{
    char current = 0;
    vector<bool> done('z');
    
    for (unsigned int i = 0; i < train.size(); i++) {
        char t = train[i];
        if (t == current)
            continue;
        else if (t < 'a' || t > 'z')
            continue;
        else if (done[t])
            return false;
        else {
            current = t;
            done[t] = true;
        }
    }
    
    return true;
}

output solve(input in, scratch sc)
{
    output out;
    
    sc.N = in.N;
    sc.cars = in.cars;
    for (int i = 0; i < sc.N; i++)
        sc.cars[i] += 'A' + (char)i;
    sort(sc.cars.begin(), sc.cars.end());
    
    do {
        string train = accumulate(sc.cars.begin(), sc.cars.end(), string());
//        cerr << train << endl;
        if (is_valid(train))
            out.W++;
    } while (next_permutation(sc.cars.begin(), sc.cars.end()));
    
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
