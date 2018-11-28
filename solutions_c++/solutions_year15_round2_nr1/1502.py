#include <bits/stdc++.h>
#define ll long long
#define f first
#define s second
using namespace std;

map<int,int>M;
bool vis[1000005];

priority_queue< pair<int,int> >Q;

int ar[10005];

int flip(int num)
{
    int x=0;
    while(num!=0)
    {
        x*=10;
        x+=(num%10);
        num/=10;
    }
    return x;
}



void shortest_path(int sc)
{
    M.clear();

    M[1]=1;

    int i;
    for(i=1;i<=sc;i++) vis[i]=false;

    pair<int,int>p;

    p.f=-1;
    p.s=1;

    while(!Q.empty()) Q.pop();

    Q.push(p);

    int b,c,d,e,x,y,z;

    while(!Q.empty())
    {
        p=Q.top(); Q.pop();

        b=p.s; d=p.f*-1;

        if(vis[b]) continue; vis[b]=true;

        if(b==sc) break;

        if(!vis[b+1])
        {
            M[b+1]=d+1;
            p.s=b+1;
            p.f=-1*M[b+1];
            Q.push(p);
        }
        else
        {
            if(d+1<M[b+1])
            {
                M[b+1]=d+1;
                p.s=b+1;
                p.f=-1*M[b+1];
                Q.push(p);
            }
        }
        x=flip(b);
        if(x>sc) continue;
        if(!vis[x])
        {
            M[x]=d+1;
            p.s=x;
            p.f=-1*M[x];
            Q.push(p);
        }
        else
        {
            if(d+1<M[x])
            {
                M[x]=d+1;
                p.s=x;
                p.f=-1*M[x];
                Q.push(p);
            }
        }
    }
    cout<<M[sc]<<endl;
}

int main()
{

    freopen("A-small-attempt1.in","r",stdin);
    freopen("A.out","w",stdout);

    int it,T;

	ll n;

    scanf("%d",&T);

	for(it=1;it<=T;it++)
	{


	    cin>>n;

        printf("Case #%d: ",it);
	    shortest_path(n);

	}

    return 0;
}
