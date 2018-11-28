#include<bits/stdc++.h>                         //Author: Sharad Chandran
#define lld long long int                       //Handle: sharad07
#define llu unsigned long long int
#define pb(x) push_back(x)
#define pii pair<int,int>
#define pll pair<lld,lld>
#define pq priority_queue<int> 
#define mp(x,y) make_pair(x,y)
#define sz size()
#define inp1(x) scanf("%d",&x)
#define inp2(x,y) scanf("%d%d",&x,&y)
#define inp3(x,y,z) scanf("%d%d%d",&x,&y,&z)
#define print(x) printf("%d",x)
#define println(x) printf("%d\n",x)
#define _for(i,x,y) for(int i=x;i<y;i++)
using namespace std;
const int maxx=1e5+3;
lld mod=1e9+7;

struct util
{
    char ch;
    int num;
};

inline bool cmp(const util &a,const util &b)
{
    return a.num>b.num;
}

void solve()
{
    int N;
    cin>>N;
    int ctr=0;
    util A[26];
    _for(i,0,N) 
    {
        cin>>A[i].num;
        A[i].ch=(char)('A'+i);
        ctr+=A[i].num;
    }
    while(ctr>2)
    {
        sort(A,A+N,cmp);
        if(A[0].num==A[1].num&&A[0].num>1)
        {
            cout<<A[0].ch<<A[1].ch<<" ";
            A[0].num--; A[1].num--;
            ctr-=2;
        }
        else 
        {
            cout<<A[0].ch<<" ";
            A[0].num--;
            ctr-=1;
        }
    }
    sort(A,A+N,cmp);
    if(N==1) cout<<A[0].ch<<A[0].ch;
    else if(N>1) cout<<A[0].ch<<A[1].ch;
    else cout<<A[0].ch;
    cout<<endl;
}

int main()
{
    freopen("A.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    _for(tc,1,t+1)
    {
        printf("Case #%d: ",tc);
        solve();
    }
    return 0;
}