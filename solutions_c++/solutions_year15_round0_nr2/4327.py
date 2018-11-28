#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <set>
using namespace std;

map<multiset<int>, int> memo;
int func(multiset<int> q)
{
    if (-*q.begin()<3) return -*q.begin();

    if (memo.count(q)) return memo[q];
    int p=-*q.begin();
    q.erase(q.begin());
    int res=p;
    for(int i=2;i<=p/2;++i) {
        q.insert(-i);
        q.insert(i-p);
        res=min(res, func(q)+1);
        q.erase(q.find(-i));
        q.erase(q.find(i-p));
    }
    return memo[q]=res;
}

int main()
{
    int T; cin>>T;
    for(int x=1;x<=T;++x) {
        int n; cin>>n;
        memo.clear();
        multiset<int> q;
        while (n--) { int p; cin>>p; q.insert(-p); }
        printf("Case #%d: %d\n", x, func(q));
    }
}

