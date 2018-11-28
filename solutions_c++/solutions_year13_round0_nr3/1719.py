#define _USE_MATH_DEFINES

#include <iostream>
#include <fstream>

#include <algorithm>
#include <functional>
#include <utility>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <string>
#include <sstream>
#include <iterator>
#include <cmath>

template<typename T> T fromString(const std::string &str)
{
    T x;
    std::stringstream(str) >> x;
    return x;
}

class MakeString
{
public:
    MakeString() : stream(){}
    template<class T>
    MakeString& operator<< (const T &arg)
    {
        stream << arg;
        return *this;
    }
    operator std::string() const
    {
        return stream.str();
    }
protected:
    std::stringstream stream;
};

/*
SOLUTION BEGIN
*/
using namespace std;

typedef long long ll;

ll rev(ll x)
{
    ll r = 0;
    ll d;
    while(x > 0)
    {
        d = x % 10;
        r = r * 10 + d;
        x = x / 10;
    }
    return r;
}

inline bool pali(long long a)
{
    return (rev(a) == a);
}

vector<int> p;

int main(int argc, char **argv, char **envp)
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios::sync_with_stdio(false);

    vector<ll> G;

    for(long long i = 1; i < 100 * 1000 * 1000; ++i)
    {
        if(pali(i) && pali(i * i))
        {
            G.push_back(i * i);
        }
    }

    int T;
    cin >> T;

    for(int t = 0; t < T; ++t)
    {
        ll A, B;
        cin >> A >> B;
        cout << string(MakeString() << "Case #" << t + 1 << ": ");
        int ans = 0;
        for(int i = 0; i < G.size(); ++i)
            if(A <= G[i] && G[i] <= B)
                ++ans;
        cout << ans << endl;
    }

    return 0;
}