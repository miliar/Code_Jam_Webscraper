#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <algorithm>
#include <stack>
#include <vector>


using namespace std;

ifstream in("small_C.in");
ofstream out("small_C.out");

int a[10][10];

string zipCodes[10];

int n;

string answer, s;

void print(const vector <int>& b)
{
    for (int i = 0; i < b.size(); ++i)
        cout << b[i];
}

bool check(const vector <int>& p, int hamar, stack <int> st)
{
    //cout << hamar << endl;
    if (hamar == n - 1)
        return true;
   
    while (!st.empty())
    {
        int g = st.top();
        if (a[g][p[hamar + 1]] == 1)
        {
            st.push(p[hamar + 1]);
            if (check(p, hamar + 1, st))
                return true;
            st.pop();
        }
        st.pop();
    }
    return false;
}

bool solve(const vector <int>& p)
{
    stack <int> st;
    st.push(p[0]);
    return check(p, 0, st);
}

int main()
{
	int test, t, m;
	in >> test;
	for (t = 1; t <= test; ++t)
	{
        for (int i = 0; i < 10; ++i)
            for (int j = 0; j < 10; ++j)
                a[i][j] = 0;

        in >> n >> m;
        
        for (int i = 0; i < n; ++i)
            in >> zipCodes[i];

        for (int i = 0; i < m; ++i)
        {
            int u, v;
            in >> u >> v;
            a[u - 1][v - 1] = 1;
            a[v - 1][u - 1] = 1;
        }

        answer = "";

        vector <int> p(n);
        for (int i = 0; i < n; ++i)
            p[i] = i;

        do
        {
            s = "";
            for (int i = 0; i < n; ++i)
                s = s + zipCodes[p[i]];                        
            if (solve(p))
                if (answer == "" || s < answer)
                    answer = s;
        } while (next_permutation(p.begin(), p.end()));

        out << "Case #" << t << ": " << answer << endl;       
    }

	return 0;
}