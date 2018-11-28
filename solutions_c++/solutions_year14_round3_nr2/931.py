#include<fstream>
#include<string>
#include<iostream>
using namespace std;

int v[15], N, contor, T;
string s[15], z;

ifstream f("B-small-attempt0.in");
ofstream g("output.txt");

bool valid(int k)
{
    for (int i = 1; i < k;i++)
        if (v[i] == v[k])
            return 0;
    return 1;
}

bool good()
{
    bool vis[256];
    for (int i = 0; i < 256; i ++)
        vis[i] = false;
    z = "";
    for (int i = 1; i <= N; i ++)
        z += s[v[i]];
    vis[z[0]] = true;
    for (int i = 1; i < z.size(); i ++)
        if (z[i] != z[i - 1] && vis[z[i]])
            return false;
        else
            vis[z[i]] = true;
    return true;
}

void Back(int k)
{
    for (int i = 1; i <= N; i++)
    {
        v[k] = i;

        if (valid(k))
        {
            if (k == N)
            {
                if (good())
                    contor ++;
            }
            else
                if (k < N)
                    Back(k + 1);
        }
    }
}

int main()
{
    f >> T;
    for (int i = 1; i <= T; i ++)
    {
        f >> N;
        for (int j = 1; j <= N; j ++)
            f >> s[j];
        contor = 0;
        Back(1);
        g << "Case #" << i << ": " << contor << endl;
    }
    f.close();
    g.close();
    return 0;
}
