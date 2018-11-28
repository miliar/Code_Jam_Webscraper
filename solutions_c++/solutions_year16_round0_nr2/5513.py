#include <bits/stdc++.h>
#define endl '\n'
using namespace std;

const int maxN = 1030;

struct edge
{
    int node_to, time;

    edge(){}
    edge(int node_to, int time)
    {
        this->node_to = node_to;
        this->time = time;
    }
};

bool vis[maxN];
int t, n, ans;

int convert_to_dec(string s)
{
    int current_multi = 1, dec = 0;

    for(int i = n - 1; i >= 0; i--)
    {
        dec += current_multi * (s[i] == '1' ? 1 : 0);
        current_multi *= 2;
    }

    return dec;
}
string convert_to_bin(int dec)
{
    string bin;

    while(dec > 0)
    {
        if(dec % 2 == 0) bin += '0';
        else bin += '1';

        dec /= 2;
    }

    reverse(bin.begin(), bin.end());
    while(bin.size() != n) bin = '0' + bin;

    return bin;
}
string make_operation(int cnt, string original)
{
    string new_string = original;
    reverse(new_string.begin(), new_string.begin() + cnt);

    for(int i = 0; i < cnt; i++)
    {
        if(new_string[i] == '1') new_string[i] = '0';
        else new_string[i] = '1';
    }

    return new_string;
}
void bfs(int start_node)
{
    queue<edge> q;
    q.push(edge(start_node, 0));

    while(!q.empty())
    {
        int current_node = q.front().node_to, current_time = q.front().time;
        q.pop();

        if(current_node == (1 << n) - 1)
        {
            ans = current_time;
            return;
        }

        if(vis[current_node]) continue;
        else vis[current_node] = true;

        string current_bin = convert_to_bin(current_node), new_string;

        for(int i = 1; i <= n; i++)
        {
            new_string = make_operation(i, current_bin);
            q.push(edge(convert_to_dec(new_string), current_time + 1));
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin>>t;
    for(int cs = 1; cs <= t; cs++)
    {
        string s;
        cin>>s;
        n = s.size();

        for(int i = 0; i < n; i++)
        {
            if(s[i] == '+') s[i] = '1';
            else s[i] = '0';
        }

        memset(vis, 0, sizeof(vis));

        int start_node = convert_to_dec(s);
        bfs(start_node);

        cout<<"Case #"<<cs<<": "<<ans<<endl;
    }

    return 0;
}
