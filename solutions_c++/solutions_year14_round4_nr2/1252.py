#include <bits/stdc++.h>

using namespace std;

int N;
set<vector<int>> seen;
struct blah
{
    vector<int> data;
    blah():
        data(N)
    {
        //
    }
};
queue<blah> Q;

bool check(blah b)
{
    int idx=max_element(b.data.begin(), b.data.end())-b.data.begin();
    for(int i=0; i<idx-1; i++)
        if(b.data[i]>b.data[i+1])
            return false;
    for(int i=N-1; i>idx+1; i--)
        if(b.data[i]>b.data[i-1])
            return false;
    return true;
}

void solve()
{
    seen.clear();
    cin>>N;
    blah orig;
    for(int i=0; i<N; i++)
        cin>>orig.data[i];
    Q=queue<blah>();
    Q.push(orig);
    int ans=0;
    if(check(orig))
        goto done;
    seen.insert(orig.data);
    while(!Q.empty())
    {
        int temp=Q.size();
        while(temp--)
        {
            blah cur=Q.front();
            Q.pop();
            for(int i=0; i<N-1; i++)
            {
                swap(cur.data[i], cur.data[i+1]);
                if(!seen.count(cur.data))
                {
                    if(check(cur))
                    {
                        ans++;
                        goto done;
                    }
                    seen.insert(cur.data);
                    Q.push(cur);
                }
                swap(cur.data[i+1], cur.data[i]);
            }
        }
        ans++;
    }
    done:;
    printf("%d\n", ans);
}

int main()
{
    freopen("..\\Google_Code_Jam\\B-small-attempt2.in", "r", stdin);
    freopen("..\\Google_Code_Jam\\B-small-attempt2.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int i=1; i<=T; i++)
    {
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
