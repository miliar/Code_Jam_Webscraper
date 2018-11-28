#include <bits/stdc++.h>
#define inf 1000000000
#define ll long long

using namespace std;

int r,c,ret;
map < vector <vector <int> >  , bool > mymap;
vector <vector <int> > vv;

int dx[4]={0,0,1,-1};
int dy[4]={1,-1,0,0};

bool valid(int x,int y)
{
    return (x>=0 && x<r && y>=0 && y<c);
}

bool match()
{
    vector <vector<int> > nvv;

    int i,j,k,x,y;

    nvv = vv;

    for(i=0;i<c;i++)
    {
        for(x=0;x<r;x++)
        {
            for(y=0;y<c;y++)
            {
                nvv[x][y] = vv[x][(y+i)%c];
            }
        }

        if(mymap[nvv]) return 1;
    }

    return 0;
}

void show()
{
    int i,j,k;

    for(i=0;i<r;i++)
    {
        for(j=0;j<c;j++)
        {
            printf("%d ",vv[i][j]);
        }
        printf("\n");
    }

    printf("\n\n");
}

bool finalCheck()
{
    int i,j,k,nx,ny,val,cnt;

    for(i=0;i<r;i++)
    {
        for(j=0;j<c;j++)
        {
            val = vv[i][j];
            cnt = 0;

            if(val==0) continue;

            for(k=0;k<4;k++)
            {
                nx=i+dx[k];
                ny=(j+dy[k]+c)%c;

                if(!valid(nx,ny)) continue;

                cnt += (vv[nx][ny]==val);
            }

            if(cnt !=val) return 0;
        }
    }

    return 1;

}

bool check()
{
    int i,j,k,nx,ny,val,cnt,zero;

    for(i=0;i<r;i++)
    {
        for(j=0;j<c;j++)
        {
            val = vv[i][j];
            cnt = 0;
            zero = 0;

            if(val==0) continue;

            for(k=0;k<4;k++)
            {
                nx=i+dx[k];
                ny=(j+dy[k]+c)%c;

                if(!valid(nx,ny)) continue;

                cnt += (vv[nx][ny]==val);
                if(vv[nx][ny]==0) zero++;
            }

            if(cnt+zero<val) return 0;
            if(cnt>val) return 0;
        }
    }

    return 1;

}


void solve(int x,int y)
{

    int i,j,k,nx,ny,cnt[4];

    if(x==r)
    {
        if(!finalCheck()) return;

        if(!match())
        {
            ret++;
            mymap[vv]=1;
            //show();
        }

        return;

    }

    if(!check()) return;

    for(i=0;i<=3;i++) cnt[i]=0;

    for(i=0;i<4;i++)
    {
        nx=x+dx[i];
        ny=(y+dy[i]+c)%c;

        if(!valid(nx,ny)) continue;

        cnt[vv[nx][ny]]++;
    }



    for(k=1;k<=3;k++)
    {
        if(cnt[0]+cnt[k]>=k  && cnt[k]<=k)
        {
            vv[x][y]=k;

            solve(x+(y==(c-1)),(y+1)%c);

            vv[x][y]=0;
        }

    }

}

int main()
{
    int i,j,k,Test,cas;

    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small.txt","w",stdout);

    scanf("%d",&Test);


    for(cas=1;cas<=Test;cas++)
    {
        scanf("%d %d",&r,&c);

        vector <int> v;

        for(ret=i=0;i<c;i++) v.push_back(0);

        vv.clear();

        for(i=0;i<r;i++) vv.push_back(v);

        mymap.clear();

        solve(0,0);

        printf("Case #%d: %d\n",cas,ret);

    }

    return 0;
}
