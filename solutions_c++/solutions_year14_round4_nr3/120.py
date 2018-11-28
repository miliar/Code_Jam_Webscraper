//Przemysław Jakub Kozłowski
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#define FI first
#define SE second
#define MP make_pair
using namespace std;
typedef long long LL;
typedef pair<pair<int,int>, pair<int,int> > PROS;
const int MB = 1003;
const LL LINF = 100000000000000018LL;

int t;
int W, H, B;
PROS tab[MB+7];
vector<pair<int,int> > V[MB+7];
LL odl[MB+7];

struct cmp
{
    bool operator()(const pair<int, LL> &a, const pair<int, LL> &b) const
    {
        return a.SE > b.SE;
    }
};
void dijkstra(int x)
{
    priority_queue<pair<int, LL>, vector<pair<int, LL> >, cmp> K;

    for(int i = 0;i <= B+1;i++) odl[i] = LINF;

    odl[x] = 0;
    K.push(MP(x, 0));

    while(!K.empty())
    {
        pair<int, LL> k = K.top();
        K.pop();

        if(odl[k.FI] < k.SE) continue;

        for(int i = 0;i < V[k.FI].size();i++)
            if(k.SE+V[k.FI][i].SE < odl[V[k.FI][i].FI])
            {
                odl[V[k.FI][i].FI] = k.SE+V[k.FI][i].SE;
                K.push(MP(V[k.FI][i].FI, odl[V[k.FI][i].FI]));
            }
    }
}

int podl(PROS A, PROS B)
{
    if(A.FI.FI > B.FI.FI) swap(A,B);
    int ret = 0;
    if(A.SE.SE < B.FI.SE) ret += B.FI.SE-A.SE.SE-1;
    if(B.SE.SE < A.FI.SE) ret += A.FI.SE-B.SE.SE-1;
    if(A.SE.FI < B.FI.FI) ret += B.FI.FI-A.SE.FI-1;

    if(A.SE.FI < B.FI.FI)
    {
        if(A.SE.SE < B.FI.SE) ret = min(ret, max(B.FI.SE-A.SE.SE-1, B.FI.FI-A.SE.FI-1));
        if(B.SE.SE < A.FI.SE) ret = min(ret, max(A.FI.SE-B.SE.SE-1, B.FI.FI-A.SE.FI-1));
    }

    return ret;
}

void kra(int a, int b, int c)
{
    V[a].push_back(MP(b,c));
    V[b].push_back(MP(a,c));
}

int main()
{
    scanf("%d", &t);
    for(int ti = 1;ti <= t;ti++)
    {
        scanf("%d%d%d", &W, &H, &B);
        for(int i = 1;i <= B;i++)
            scanf("%d%d%d%d", &tab[i].FI.FI, &tab[i].FI.SE, &tab[i].SE.FI, &tab[i].SE.SE);

        for(int i = 0;i <= B+1;i++) V[i].clear();

        kra(0, B+1, W);
        for(int i = 1;i <= B;i++)
        {
            kra(0, i, tab[i].FI.FI);
            kra(i, B+1, W-tab[i].SE.FI-1);
        }
        for(int i = 1;i <= B;i++)
            for(int j = i+1;j <= B;j++)
            {
                //cerr << "I: " << i << " J: " << j << " odl: " << podl(tab[i], tab[j]) << endl;
                kra(i,j, podl(tab[i], tab[j]));
            }
        dijkstra(0);

        printf("Case #%d: %lld\n", ti, odl[B+1]);
    }
    return 0;
}
