#include <iostream>
#include <queue>
#include <string>

using namespace std;

const int maxlen=2000;
int mark[maxlen];
int dist[maxlen];

string right_child(string a, int x)
{
    string ans = "";
    for (int i = x; i>= 0; i--)
        ans += (a[i]=='-')? '+': '-';
    for (int i = x+1; i < a.size(); ++i)
        ans += a[i];
    return ans;
}
string left_child(string a, int x)
{
    string ans = "";
    for (int i = x+1; i < a.size(); ++i)
        ans += a[i];
    for (int i = x; i>= 0; i--)
        ans += (a[i]=='-')? '+': '-';
    return ans;
}

int to_int(string a)
{
    int ans = 0;
    for (int i=0; i < a.size(); ++i)
        if (a[i] == '-')
            ans |= (1<<i);
    return ans;
}
int bfs(string x)
{
    memset(mark, 0, sizeof(mark));
    memset(dist, 0, sizeof(dist));
    queue<string> q;
    q.push(x);
    mark[to_int(x)] = 1; dist[to_int(x)] = 0;
    while (!q.empty()) {
        string v = q.front();
        q.pop();
        if (to_int(v) == 0)
            return dist[to_int(v)];
        for (int i=0; i<v.size(); ++i) {
            string s1 = right_child(v, i);
            string s2 = left_child(v, i);
            if (!mark[to_int(s1)]) {
                q.push(s1);
                mark[to_int(s1)] = 1;
                dist[to_int(s1)] = dist[to_int(v)]+1;
                //cout <<"right, form" << v << " "<<s1 << endl;
            }
            /*if (!mark[to_int(s2)]) {
                q.push(s2);
                mark[to_int(s2)] = 1;
                dist[to_int(s2)] = dist[to_int(v)]+1;
                cout <<"left, form" << v << " "<<s2 << endl;
            }*/
        }
    }
    return -1;
}

int main()
{
    int t; cin>>t;
    int i = 1;
    while (t--) {
        string s; cin>>s;
        int ans = bfs(s);
        cout<<"Case #"<<i<<": "<<ans<<endl;
        i++;
    }
    return 0;
}
