#include <fstream>
#include <queue>
using namespace std;

struct cmp
{
    bool operator()(const pair<int, int> &a, const pair<int, int> &b)
    {
        return a.first < b.first;
    }
};
int main()
{
    ifstream f("input.in");
    ofstream g("output.out");

    int T, N, i, j, sum, x;
    f >> T;
    for (i = 1; i <= T; i++)
    {
        f >> N;
        priority_queue<pair<int, int>, vector<pair<int, int>>, cmp> pq;
        for (j = 0; j < N; j++)
        {
            f >> x;
            pq.push({x, j});
            sum += x;
        }

        g << "Case #" << i << ": ";
        while (!pq.empty())
        {
            pair<int, int> p = pq.top();
            g << char(p.second + 'A');
            pq.pop();
            sum--;
            p.first--;
            if (!pq.empty())
            {
                pair<int, int> q = pq.top();
                if (q.first > sum / 2)
                {
                    g << char(q.second + 'A');
                    q.first--;
                    pq.pop();
                    if (q.first > 0)
                        pq.push({q.first, q.second});
                    sum--;
                }
            }
            if (p.first > 0)
                pq.push({p.first, p.second});
            g << " ";
        }
        g << '\n';
    }
    f.close();
    g.close();
    return 0;
}
