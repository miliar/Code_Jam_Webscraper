#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <algorithm>
using namespace std;

const int MAXN=201;
int num[401];
class Chest
{
public:
    int type;
    vector<int> keys;
};
Chest c[MAXN];
bool used[MAXN];
vector<int> res;
vector<int> stack;
bool exist[1<<21];

void search(int depth,int N,int mask)
{
    //char buf[50];
    //itoa(mask, buf, 2);
    //printf("mask=%s\n",buf);
    //printf("depth=%d\n stack= ",depth);
    //for (int i=0;i<stack.size();i++)
    //{
    //    printf(" %d",stack[i]);
    //}printf("\n");
    if (depth>=N)
    {
        res.clear();
        for (int i=0;i<stack.size();i++)
        {
            res.push_back(stack[i]);
        }
        return;
    }
    if (res.size()>=N) return; 
    exist[mask]=true;  
    for (int i=1;i<=N;i++)
    {
        if (used[i]) continue;
        if (num[c[i].type]<=0) continue;
        int tmp=(mask+(1<<(i-1)));
        if (exist[tmp]) continue;
        num[c[i].type]--;
        stack.push_back(i);
        used[i]=true;
        for (int j=0;j<c[i].keys.size();j++)
        {
            int k=c[i].keys[j];
            num[k]++;
        }
        //printf("i=%d\n",i);
        search(depth+1,N,tmp);
        stack.pop_back();
        num[c[i].type]++;
        used[i]=false;
        for (int j=0;j<c[i].keys.size();j++)
        {
            int k=c[i].keys[j];
            num[k]--;
        }
    }
}
int main()
{
    int T,K,N;
    int d,M;
    freopen("D-small-attempt2.in","r",stdin);
    freopen("D_output_small.txt","w",stdout);
    scanf("%d",&T);
    for (int cases=1;cases<=T;cases++)
    {
        scanf("%d%d",&K,&N);
        memset(num,0,sizeof(num));
        for (int i=0;i<K;i++)
        {
            scanf("%d",&d);
            num[d]++;
        }
        for (int i=1;i<=N;i++)
        {
            scanf("%d",&c[i].type);
            c[i].keys.clear();
            scanf("%d",&M);
            for (int j=0;j<M;j++)
            {
                scanf("%d",&d);
                c[i].keys.push_back(d);
            }
        }
        printf("Case #%d:",cases);
        memset(used,0,sizeof(used));
        res.clear();
        stack.clear();
        memset(exist,0,sizeof(exist));
        search(0,N,0);
        if (res.size()==0) printf(" IMPOSSIBLE\n");
        else{
            for (int i=0;i<res.size();i++) printf(" %d",res[i]);
            printf("\n");
        }
    }
    return 0;
}
