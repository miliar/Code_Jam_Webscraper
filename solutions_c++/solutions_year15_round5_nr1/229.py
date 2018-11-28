#include <bits/stdc++.h>
#define inf 1000000000
#define ll long long
#define Max 200005

using namespace std;

int n,d,sal[Max],par[Max],mxsal;
vector <int> child[Max];
ll M[Max];
bool active[Max];
int tree[Max];

int read(int idx){
    int sum = 0;
    while (idx > 0){
        sum += tree[idx];
        idx -= (idx & -idx);
    }
    return sum;
}

void update(int idx ,int val){
    while (idx <= mxsal+2){
        tree[idx] += val;
        idx += (idx & -idx);
    }
}

void work(int x,int y)
{
    int i,j,k,p,q;

    p=y-d;

    q = x;

    if(p<1) p = 1;

    if(q<p) return;

    update(p,1);
    update(q+1,-1);


}

void dfs(int x,int mn,int mx)
{
    int i,j,k;

   // cout<<x<<" "<<mn<<" "<<mx<<endl;

    work(mn,mx);

    for(i=0;i<child[x].size();i++)
    {
        j=child[x][i];

        dfs(j,min(mn,sal[j]),max(mx,sal[j]));
    }
}

int main()
{
    int i,j,k,Test,cas,ret=0;
    ll so,as,cs,rs,mo,am,cm,rm;

    //freopen("in.txt","r",stdin);
    freopen("A-small-attempt0(1).in","r",stdin);
    freopen("Asmall.txt","w",stdout);

    scanf("%d",&Test);


    for(cas=1;cas<=Test;cas++)
    {

        scanf("%d %d",&n,&d);

        memset(tree,0,sizeof(tree));

        cin>>so>>as>>cs>>rs;
        cin>>mo>>am>>cm>>rm;

        sal[0]=so;
        M[0]=mo;
        child[0].clear();

        for(i=1;i<n;i++)
        {
            child[i].clear();
            sal[i] = (sal[i-1]*as+cs)%rs;
            M[i] = (M[i-1]*am+cm)%rm;
        }

        for(i=0;i<n;i++) sal[i]++;



        mxsal = sal[0];

        for(i=1;i<n;i++)
        {
            mxsal = max(mxsal , sal[i]);
            par[i] = M[i]%i;

            child[par[i]].push_back(i);
        }

        //for(i=0;i<n;i++) printf("%d. sal:%d , par:%d\n",i,sal[i]-1,par[i]);

        dfs(0,sal[0],sal[0]);

        ret = 0;

        for(i=1;i<=mxsal;i++) ret = max(ret , read(i));

        printf("Case #%d: %d\n",cas,ret);

    }

    return 0;
}
