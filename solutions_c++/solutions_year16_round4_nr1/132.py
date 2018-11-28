#include <bits/stdc++.h>

using namespace std;

bool isok(int r, int p, int s)
{
    if(r+p+s<=2)
        return r<=1 && p<=1 && s<=1;
    int n=r+p+s, q=n/4;
    assert(n%4==0);
    return r>=q && p>=q && s>=q && isok(s-q, r-q, p-q);
}

string recover(int r, int p, int s, int R, int P, int S)
{
    if(r+p+s<=2)
    {
        vector<pair<int, char>> ans;
        for(int i=0; i<r; i++)
            ans.push_back({R, 'R'});
        for(int i=0; i<p; i++)
            ans.push_back({P, 'P'});
        for(int i=0; i<s; i++)
            ans.push_back({S, 'S'});
        sort(ans.begin(), ans.end());
        string ret;
        for(auto& it: ans)
            ret+=it.second;
        return ret;
    }
    int q=(r+p+s)/4;
    vector<pair<pair<pair<int, int>, pair<int, int>>, int>> v;
    v.push_back({{{P, R}, {P, S}}, 2});
    v.push_back({{{P, R}, {R, S}}, 1});
    v.push_back({{{P, S}, {R, S}}, 0});
    for(auto& it: v)
    {
        {
            auto& t=it.first.first;
            if(t.first>t.second)
                swap(t.first, t.second);
            auto& t2=it.first.second;
            if(t2.first>t2.second)
                swap(t2.first, t2.second);
        }
    }
    for(auto& it: v)
    {
        auto& it2=it.first;
        if(it2.first>it2.second)
            swap(it2.first, it2.second);
    }
    sort(v.begin(), v.end());
    vector<int> w(3);
    for(int i=0; i<3; i++)
        w[v[i].second]=i;
    string seq=recover(s-q, r-q, p-q, w[0], w[1], w[2]);
    string T;
    for(auto& it: seq)
    {
        int key=-1;
        if(it=='S')
            key=2;
        else if(it=='P')
            key=1;
        else if(it=='R')
            key=0;
        else
            assert(0);
        for(auto& it2: v) if(it2.second==key)
        {
            vector<int> vv={it2.first.first.first, it2.first.first.second, it2.first.second.first, it2.first.second.second};
            for(auto& it3: vv)
            {
                if(it3==R)
                    T+='R';
                else if(it3==P)
                    T+='P';
                else if(it3==S)
                    T+='S';
            }
            break;
        }
    }
    return T;
}

void _main(int TEST)
{
    int n, r, p, s;
    scanf("%d%d%d%d", &n, &r, &p, &s);
    if(!isok(r, p, s))
        printf("IMPOSSIBLE\n");
    else
        printf("%s\n", recover(r, p, s, 1, 0, 2).c_str());
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int TEST;
    scanf("%d", &TEST);
    for(int i=1; i<=TEST; i++)
    {
        printf("Case #%d: ", i);
        _main(i);
    }
    return 0;
}
