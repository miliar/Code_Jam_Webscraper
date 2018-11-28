#include <iostream>
#include <algorithm>
#include <cmath>
#include <climits>
#include <deque>
using namespace std;

struct State
{
    int i;
    int A;
    int count;

    State(int ii, int AA, int ccount) : i(ii), A(AA), count(ccount) {}
    State(const State & r) : i(r.i), A(r.A), count(r.count) {}
};

int main()
{
    int * m = new int[100];
    int T;
    cin >> T;
    for(int k = 1; k <= T; k++)
    {
        int A,N;
        cin >> A >> N;
        for (int i = 0; i < N; i++)
            cin >> m[i];

        sort(m, m+N);

        deque<State> qs;
        qs.push_back(State(0, A, 0));
        int count_min = INT_MAX;
        while(!qs.empty())
        {
            const State & sf = qs.front();
            if(sf.i >= N)
            {
                count_min = min(count_min, sf.count);
                qs.pop_front();
            }
            else if(sf.A > m[sf.i])
            {
                qs.push_back(State(sf.i+1, sf.A+m[sf.i], sf.count));
                qs.pop_front();
            }
            else
            {
                qs.push_back(State(sf.i+1, sf.A, sf.count+1));
                if(sf.A > 1)
                    qs.push_back(State(sf.i, 2*sf.A-1, sf.count+1));
                qs.pop_front();
            }
        }

        cout << "Case #" << k << ": " << count_min << endl;
    }
    delete[] m;
    return 0;
}
