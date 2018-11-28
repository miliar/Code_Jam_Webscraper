/********************************/
/***  Coded By Ankush Sharma  ***/
/********************************/

#include<bits/stdc++.h>
using namespace std;

int dp(priority_queue<int> q, int n, int k, int c)
{
    while(c--) { q.push(n-k); q.push(k); }
    if(q.top()==1) return 1;
    if(q.top()==0) return 0;
    int ret=q.top(), limit=q.top(), count=0;
    while(q.size() && limit==q.top()) q.pop(), count++;
    for(int i=1; i<=limit/2; i++)
    {
        ret=min(ret, count+dp(q, limit, i, count));
        //if(i==4) cout<<count+dp(q, limit, i, count)<<" ";
    }
    return ret;
}

int main()
{
    //std::ios::sync_with_stdio(false);
    freopen("B-small-attempt2.in", "r", stdin);
    freopen("B-small-attempt2.out", "w", stdout);
    int t, c; cin>>t;
    c=t;
    while(t--)
    {
        int d; cin>>d;
        priority_queue<int> q;
        for(int i=0; i<d; i++)
        {
            int temp; cin>>temp;
            q.push(temp);
        }
        cout<<"Case #"<<c-t<<": "<<dp(q, 0, 0, 0)<<"\n";
    }
    return 0;
}

