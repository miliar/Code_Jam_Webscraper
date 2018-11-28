#include <fstream>
#include <cstring>

const int LMAX = 12345;

using namespace std;

ifstream f("dijkstra.in");
ofstream g("dijkstra.out");

int T,N,it,L,X,l;
char s[LMAX];
char nr;
int semn;
bool ok;

void step()
{
    if (nr == '1')
    {
        if (s[it] == 'i')
            nr = 'i';
        if (s[it] == 'j')
            nr = 'j';
        if (s[it] == 'k')
            nr = 'k';
        it++;
        return;
    }
    if (nr == 'i')
    {
        if (s[it] == 'i')
        {
            nr = '1';
            semn = -semn;
        }
        if (s[it] == 'j')
            nr = 'k';
        if (s[it] == 'k')
        {
            nr = 'j';
            semn = -semn;
        }
        it++;
        return;
    }
    if (nr == 'j')
    {
        if (s[it] == 'i')
        {
            nr = 'k';
            semn = -semn;
        }
        if (s[it] == 'j')
        {
            nr = '1';
            semn = -semn;
        }
        if (s[it] == 'k')
            nr = 'i';
        it++;
        return;
    }
    if (nr == 'k')
    {
        if (s[it] == 'i')
            nr = 'j';
        if (s[it] == 'j')
        {
            nr = 'i';
            semn = -semn;
        }
        if (s[it] == 'k')
        {
            nr = '1';
            semn = -semn;
        }
        it++;
        return;
    }

}

int main()
{
    f >> T;
    for (int t = 1; t <= T; ++t)
    {
        f >> L >> X;
        g << "Case #" << t << ": ";
        f.getline(s,123);
        f.getline(s,12343);
        l = strlen(s);
        l = X*L;
        for (int i = 0; i < L*X; ++i)
        {
            s[i] = s[i%L];
        }
        nr = s[0];
        it = 1;
        semn = 1;
        if (nr != 'i')
        {
            while(!(nr == 'i' && semn == 1) && it < l)
            {
                step();
            }
        }
        if (nr != 'i' || semn < 0)
        {
            g << "NO\n";
            continue;
        }
        nr = s[it];
        it++;
        if (nr != 'j')
        {
            while(!(nr == 'j' && semn == 1) && it < l)
            {
                step();
            }
        }
        if (nr != 'j' || semn < 0)
        {
            g << "NO\n";
            continue;
        }
        nr = s[it];
        it++;
        while(it < l)
        {
            step();
        }
        if (nr == 'k' && semn == 1)
            g << "YES\n";
        else g << "NO\n";
    }

    f.close();
    g.close();
    return 0;
}
