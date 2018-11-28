#include <bits/stdc++.h>
#define inf 1000000000
#define ll long long

using namespace std;

int tot,n,ret,cost;
map <string,int> mymap;
string str,now;
vector <int> myList[205];
int cnt[5000][2];

void solve(int x)
{

    int i,j,k;

    if(x==n+1)
    {
        for(cost=0,i=1;i<tot;i++)
        {
            if(cnt[i][0] && cnt[i][1]) cost++;
        }

        if(ret==-1 || cost<ret) ret = cost;

        return;
    }

    if(x!=2)
    {
        for(i=0;i<myList[x].size();i++)
        {
            j=myList[x][i];
            cnt[j][0]++;
        }

        solve(x+1);

        for(i=0;i<myList[x].size();i++)
        {
            j=myList[x][i];
            cnt[j][0]--;
        }

    }

    if(x!=1)
    {

        for(i=0;i<myList[x].size();i++)
        {
            j=myList[x][i];
            cnt[j][1]++;
        }

        solve(x+1);

        for(i=0;i<myList[x].size();i++)
        {
            j=myList[x][i];
            cnt[j][1]--;
        }

    }
}

int main()
{
    int i,j,k,Test,cas;

    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small.txt","w",stdout);

    scanf("%d",&Test);


    for(cas=1;cas<=Test;cas++)
    {

        tot=1;
        mymap.clear();
        scanf("%d\n",&n);

        for(i=1;i<=n;i++)
        {
            //cout<<i<<endl;
            myList[i].clear();
            std::getline (std::cin,str);
            stringstream sin(str);

            while(sin>>now)
            {
                k=mymap[now];

                //cout<<now<<endl;

                if(k==0)
                {
                    mymap[now]=tot;
                    k=tot;
                    tot++;
                }

                myList[i].push_back(k);
            }
        }

        ret=-1;
        memset(cnt,0,sizeof(cnt));

        solve(1);

        printf("Case #%d: %d\n",cas,ret);

    }

    return 0;
}
