#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N = 0;
vector<float> Naomi;
vector<float> Ken;

int DeceitfulWar()
{
    int result = 0;
    int Naomi_begin = 0, Naomi_end = N-1;
    int Ken_begin = 0, Ken_end = N-1;

    while (Naomi_begin != Naomi_end)
    {
        if (Naomi[Naomi_begin] < Ken[Ken_begin])
        {
            ++Naomi_begin;
            --Ken_end;
        }
        else
        {
            ++result;
            ++Naomi_begin;
            ++Ken_begin;
        }
    }

    // compare the last time
    if (Naomi[Naomi_begin] > Ken[Ken_begin])
    {
        ++result;
    }

    return result;
}

int War()
{
    int result = 0;
    int Naomi_begin = 0, Naomi_end = N-1;
    int Ken_begin = 0, Ken_end = N-1;

    while (Naomi_begin != Naomi_end)
    {
        if (Naomi[Naomi_end] > Ken[Ken_end])
        {
            ++result;
            --Naomi_end;
            ++Ken_begin;
        }
        else
        {
            --Naomi_end;
            --Ken_end;
        }
    }

    // compare the last time
    if (Naomi[Naomi_begin] > Ken[Ken_begin])
    {
        ++result;
    }

    return result;
}

int main()
{
    float input = 0.0;
    int T = 0;
    cin >> T;
    for (int cases = 1; cases <= T; ++cases)
    {
        cin >> N;

        Naomi.clear();
        for (int i = 0; i < N; ++i)
        {
            cin >> input;
            Naomi.push_back(input);
        }
        sort(Naomi.begin(), Naomi.end());

        Ken.clear();
        for (int i = 0; i < N; ++i)
        {
            cin >> input;
            Ken.push_back(input);
        }
        sort(Ken.begin(), Ken.end());

        cout << "Case #" << cases << ": " << DeceitfulWar() << " " << War() << endl;
    }
    return 0;
}
