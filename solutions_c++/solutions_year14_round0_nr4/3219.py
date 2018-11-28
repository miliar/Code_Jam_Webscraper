#include <iostream>
#include <string>
#include <set>

using namespace std;

int play_dw(const set<float>& nb, const set<float>& kb)
{
    set<float> n = nb;
    set<float> k = kb;

    int points = 0;
    while (!n.empty())
    {
        set<float>::reverse_iterator ina = n.rbegin();
        set<float>::iterator ike = k.upper_bound(*ina);
        if (ike == k.end())
        {
            ike = k.begin();
            n.erase(*ina);
            k.erase(ike);
            ++points;
        }
        else
        {
            n.erase(*ina);
            k.erase(ike);
        }
    }
    return points;

}

int play_w(const set<float>& nb, const set<float>& kb)
{
    set<float> n = nb;
    set<float> k = kb;
    int points = 0;
    while (!n.empty())
    {
        set<float>::reverse_iterator ina = n.rbegin();
        set<float>::reverse_iterator ike = k.rbegin();
        if (*ina > *ike)
        {
            n.erase(*ina);
            k.erase(*ike);
            ++points;
        }
        else
        {
            set<float>::iterator ina = n.begin();
            n.erase(ina);
            k.erase(*ike);
        }
    }
    return points;
}

int main (int argc, char* argv[])
{
    int T = 0;
    string dummy;
    cin >> T;
    getline(cin,dummy);

    for (int i = 0; i < T; ++i)
    {
        int N = 0;
        string dummy;
        cin >> N;
        getline(cin,dummy);

        set<float> nb;
        for (int j = 0; j < N; ++j)
        {
            float v;
            cin >> v;
            nb.insert(v);
        }

        set<float> kb;
        for (int j = 0; j < N; ++j)
        {
            float v;
            cin >> v;
            kb.insert(v);
        }

        int dw = play_dw(nb,kb);
        int w = play_w(nb,kb);

        cout << "Case #" << (i+1) << ": " << w << " " << dw << endl;
    }

    return 0;
}

