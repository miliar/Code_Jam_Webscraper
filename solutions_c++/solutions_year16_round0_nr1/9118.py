#include <bits/stdc++.h>

using namespace std;

bool W[10] = {false, false, false, false, false, false, false, false, false, false};

bool CheckDigits()
{
    for (int i = 0; i<10; i++)
        if (W[i] == false)
            return false;
    return true;
}

int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);

    int T, N=0;
    cin >> T;

    for (int i = 0; i < T; i++)
    {
        for(int l = 0; l<10; l++)
            W[l] = false;

        cin >> N;
        cin.clear();

        if (N == 0)
        {
            cout << "Case #" << i+1 << ": INSOMNIA" << endl;
            continue;
        }


        int k = 1, NC = N;

        while(!CheckDigits())
        {

            NC = N*k;

            stringstream tmp;
            tmp << NC;
            string NS(tmp.str());

            for(int j = 0; j<NS.size(); j++)
                W[(int)NS.at(j) - 48] = true;

            k++;

        }

        cout << "Case #" << i+1 << ": " << NC << endl;

    }
    return 0;
}
