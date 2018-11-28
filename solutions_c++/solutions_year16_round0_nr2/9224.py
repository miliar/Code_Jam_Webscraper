#include <bits/stdc++.h>

using namespace std;

bool CheckStack(stack<char> S)
{
    vector<char> V;
    while(!S.empty())
    {
        if(S.top() == '-')
            return false;
        S.pop();
    }
    return true;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("output.out", "w", stdout);

    int T = 0;
    cin >> T;

    for(int i = 0; i<T; i++)
    {
        stack<char> S;
        string tmp;
        cin >> tmp;
        cin.clear();

        for(int j = tmp.size()-1; j>=0; j--)
            S.push(tmp.at(j));

        int N = 0;

        while(!CheckStack(S))
        {
            vector<char> V;
            while(!S.empty())
            {
                if(V.empty())
                {
                    V.push_back(S.top());
                    S.pop();
                }
                else if(S.top() == V[0])
                {
                    V.push_back(S.top());
                    S.pop();
                }
                else
                    break;
            }

            while(!V.empty())
            {
                S.push(V.back() == '-' ? '+' : '-');
                V.pop_back();
            }

            N++;
        }

        cout << "Case #" << i+1 << ": " << N << endl;
    }

    return 0;
}
