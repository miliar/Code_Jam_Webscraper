#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <list>
using namespace std;

const int INF = 100000000;
const int MAXN = 3000;

int T, N;
bool num[MAXN];
vector<int> ans;

void solve(int qid)
{
    for(int i=1;i<=2500;i++)
        if( num[i] == true )
            ans.push_back(i);
    sort(ans.begin(),ans.end());
    cout << "Case #" << qid << ": ";
    for(int i=0;i<ans.size();i++)
        cout << ans[i] << " ";
    cout << endl;
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large-output.txt","w",stdout);

    scanf("%d",&T);
    for(int i=1;i<=T;i++)
    {
        memset(num,false,sizeof(num));
        ans.clear();
        scanf("%d",&N);
        for(int j=1;j<=N*2-1;j++)
        {
            for(int k=1;k<=N;k++)
            {
                int tmp;
                scanf("%d",&tmp);
                if( num[tmp] == true ) num[tmp] = false;
                else if( num[tmp] == false ) num[tmp] = true;
            }
        }
        solve(i);
    }

    return 0;
}
