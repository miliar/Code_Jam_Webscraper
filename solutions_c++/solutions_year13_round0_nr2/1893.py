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

int n, m;

bool H[100];
bool V[100];

int M[100][100];

void f(int h)
{
    for(int i = 0; i < 100; ++i)
    {
        H[i] = true;
        V[i] = true;
    }
    for(int i = 0; i < n; ++i)
    {
        for(int j = 0; j < m; ++j)
        {
            if(M[i][j] > h)
            {
                H[i] = false;
                V[j] = false;
            }
        }
    }
}

int main(int argc, char **argv, char **envp)
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios::sync_with_stdio(false);

    int T;
    cin >> T;

    for(int t = 0; t < T; ++t)
    {
        cin >> n >> m;

        for(int i = 0; i < n; ++i)
            for(int j = 0; j < m; ++j)
                cin >> M[i][j];

        cout << string(MakeString() << "Case #" << t + 1 << ": ");

        bool ok = true;

        for(int h = 100; h >= 0; --h)
        {
            f(h);
            for(int i = 0; i < n; ++i)
                for(int j = 0; j < m; ++j)
                    if(M[i][j] == h && H[i] == false && V[j] == false)
                    {
                        ok = false;
                    }
        }

        if(ok)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }

    return 0;
}