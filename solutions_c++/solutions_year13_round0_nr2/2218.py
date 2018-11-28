#include <cstdio>
#include <queue>
using namespace std;

int main()
{
    int s[111][111];
    int flag[111][111];
    int n,m;
    int t, caseno=0;
    int i, j;
    pair<int, pair<int, int> > pp;
    int x, y;
    int temp;
    priority_queue< pair<int, pair<int, int> > , vector<pair<int, pair<int, int> > >, greater< pair<int, pair<int, int> > > > pq;
    scanf("%d", &t);
    while (t--) {
        while(!pq.empty())
            pq.pop();
        scanf("%d%d", &n, &m);
        for (i=0; i<n; i++) {
            for (j=0; j<m; j++) {
                scanf("%d", &s[i][j]);
                flag[i][j]=0;
                pq.push(make_pair(s[i][j], make_pair(i, j)));
            }
        }
        while (!pq.empty()) {
           pp=pq.top();
           pq.pop();
           x=pp.second.first;
           y=pp.second.second;
           if(flag[pp.second.first][pp.second.second]==1)
               continue;
           temp=0;
           for(i=0; i<m; i++) {
               if(flag[x][i]==0 && s[x][i]!=pp.first) {
                   temp=1;
                   break;
               }
           }
           if(temp==0) {
               for(i=0; i<m; i++) {
                   flag[x][i]=1;
               }
               continue;
           }
           temp=0;
           for(i=0; i<n; i++) {
               if(flag[i][y]==0 && s[i][y]!=pp.first) {
                   temp=1;
                   break;
               }
           }
           if(temp==0) {
               for(i=0; i<n; i++) {
                   flag[i][y]=1;
               }
               continue;
           }
           break;
        }
        printf("Case #%d: ", ++caseno);
        if(pq.empty()) {
            printf("YES\n");
        }
        else {
            printf("NO\n");
        }
    }
    return 0;
}
