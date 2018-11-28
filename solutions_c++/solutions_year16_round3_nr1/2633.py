#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t, n, tmp, sm;
    pair<int,int> gr;
    string s;
    priority_queue<pair<int,int> > pq;
    scanf("%d", &t);
    for(int j = 1; j <= t; j++){
        s = "";
        sm = 0;
        scanf("%d", &n);
        for(int i = 0; i < n; i++){
            scanf("%d", &tmp);
            pq.push(make_pair(tmp, i));
            sm += tmp;
        }
        while(!pq.empty()){
            gr = pq.top();
            pq.pop();
            --gr.first;
            --sm;
            s += (char)('A' + gr.second);
            if(sm % 2 == 0)s += ' ';
            if(gr.first)pq.push(gr);
        }
        printf("Case #%d: %s\n", j, s.c_str());
    }
    return 0;
}
