#include<iostream>
#include<queue>
#include<cstring>
#include<algorithm>
#include<vector>
using namespace std;

int n;
int d;

int manager[1000001];
int salary[1000001];

vector<vector<int> > a_children;
vector<vector<int> > c_children; // candidates

priority_queue<pair<int,int> > next_to_enter;
priority_queue<pair<int,int> > next_to_exit;

bool removed[1000001];

int l;
int r;
int c;

void remove_rec(int i)
{
    // cout << "removing " << i << " (" << salary[i] << ")" << endl;
    if (removed[i])
        return;
    removed[i] = true;
    c -= 1;
    for (int j = 0; j < a_children[i].size(); j += 1)
    {
        int x = a_children[i][j];
        remove_rec(x);
    }
}

void do_step()
{
    while (!next_to_enter.empty() && -next_to_enter.top().first <= r)
    {
        pair<int,int> t = next_to_enter.top();
        next_to_enter.pop();
        int i = t.second;
        // cout << i << " (" << salary[i] << ", " << manager[i] << ") is entering" << endl;
        if (removed[manager[i]])
        {
            // cout << "but its manager is already out" << endl;
            continue;
        }
        a_children[manager[i]].push_back(i);
        next_to_exit.push(make_pair(-salary[i], i));
        c += 1;
        for (int j = 0; j < c_children[i].size(); j += 1)
        {
            int x = c_children[i][j];
            next_to_enter.push(make_pair(-salary[x], x));
            // cout << "also putting " << x << " (" << salary[x] << ")" << endl;
        }
    }
    while (!next_to_exit.empty() && -next_to_exit.top().first < l)
    {
        pair<int,int> t = next_to_exit.top();
        next_to_exit.pop();
        remove_rec(t.second);
    }
}

int run()
{
    cin >> n >> d;
    int s_0, a_s, c_s, r_s, m_0, a_m, c_m, r_m;
    cin >> s_0 >> a_s >> c_s >> r_s >> m_0 >> a_m >> c_m >> r_m;

    a_children.assign(n, vector<int> ());
    c_children.assign(n, vector<int> ());
    while (!next_to_enter.empty())
        next_to_enter.pop();
    while (!next_to_exit.empty())
        next_to_exit.pop();
    memset(removed, 0, sizeof(removed));

    int s_i = s_0;
    int m_i = m_0;
    for (int i = 1; i < n; i += 1)
    {
        s_i = (s_i * a_s + c_s) % r_s;
        m_i = (m_i * a_m + c_m) % r_m;

        // cout << s_i << " " << m_i << endl;

        manager[i] = m_i % i;
        salary[i] = s_i;
        c_children[m_i % i].push_back(i);
        if (m_i % i == 0)
            next_to_enter.push(make_pair(-s_i, i));
    }

    l = s_0 - d;
    r = s_0;
    c = 1;
    
    int res = 1;

    do_step();
    res = max(res, c);
    while (!next_to_enter.empty() && -next_to_enter.top().first <= s_0 + d)
    {
        r = -next_to_enter.top().first;
        l = r - d;
        do_step();
        res = max(res, c);
    }
    return res;
}

int main ()
{
    int tc;
    cin >> tc;
    for (int i = 1; i <= tc; i += 1)
    {
        cout << "Case #" << i << ": " << run() << endl;
    }
}
