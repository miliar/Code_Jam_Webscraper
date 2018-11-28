#include <iostream>
#include <string>
#include <map>
#include <bitset>
#include <stack>
#include <queue>

using namespace std;

int n;
int inf = 2147483646;
int minimum = inf;

map<string, int> glm;

int main()
{
    int T;
    string s;
    cin >> T;

    map<string, bool> m;
    bitset<100> b;
    int ok;
    queue<pair<bitset<100>, int>> Q;
    for(int t = 1; t <= T; ++t)
    {
        b.reset();
        minimum = inf;
        ok = 0;
        cin >> s;
        n = s.length();

        for (int i = 0; i < n; ++i)
        {
            if (s[i] == '+')
            {
                ++ok;
                b[i] = true;
            }
            else if (s[i] == '-')
                b[i] = false;
        }
        for (int i = n+1; i < 100; ++i)
            b[i] = false;
        //cout << ".. " << s << b.to_string() << endl;

        m.clear();
        m[b.to_string()]=true;

        Q.push(make_pair(b, 0));
        stack<bool> S;
        while(!Q.empty())
        {
            auto p = Q.front();
            Q.pop();
            //cout << "# " << p.first.to_string() << endl;

            if (p.first.count() == n)
            {
                minimum = p.second;
                while(!Q.empty())
                    Q.pop();
            }
            else
            {

                auto pom = p.first;
                for (int i = 0; i < n; ++i) // kolejno odwracam od 1 do n nalesnikow
                {
                    for (int j = 0; j <= i; ++j)
                    {
                        if (p.first[j])
                        {
                            S.push(true);
                        }
                        else
                        {
                            S.push(false);
                        }
                    }
                    for (int j = 0; j <= i; ++j)
                    {
                        if (S.top())
                            pom[j] = false;
                        else
                            pom[j] = true;
                        S.pop();
                    }
                    if (m.find(pom.to_string()) == m.end())
                    {
                        //cout << "# " << p.first.to_string() << " " << i+1 << " " << pom.to_string() << endl;
                        m[pom.to_string()] = true;
                        Q.push(make_pair(pom, p.second + 1));
                    }
                }
            }
        }

        cout << "Case #" << t << ": " << minimum << "\n";
    }

    return 0;
}
