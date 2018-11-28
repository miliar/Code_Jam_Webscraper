#include<bits/stdc++.h>
#define pii pair<long int,long int>
#define s(x) scanf("%d",&x)
#define INF (1<<20)
#define MAX 1000008
using namespace std;
int d[MAX+5];
vector<pii> G[MAX];
inline int reverse(int number)
{
    int rev = 0;
    for(; number!=0;)
    {
        rev = rev * 10;
        rev = rev + number%10;
        number = number/10;
    }
    return rev;
}
struct comp {
    //priority queue has priority according to distance
    bool operator() (const pii &a, const pii &b) {
        return a.second > b.second;
    }
};
void addedge(long int u, long int v, long int w)
{
    G[u].push_back(make_pair(v,w));
}
void dijkstra(long int root,long int des)
{
    d[root]=0;
    bool f[MAX]={0};
    long int u,v,w;
    vector<pii> :: iterator it;
    priority_queue<pii,vector<pii>,comp> Q;
    Q.push(pii(root,0));
    while(!Q.empty())
    {
        u=Q.top().first;
        //cout<<u<<"##\n";
       // if(u==des)
        //    break;
        Q.pop();
        if(f[u]==1)  continue;
        for(it=G[u].begin(); it!=G[u].end(); it++)
        {
            v=(*it).first;
            w=(*it).second;
            //cout<<u<<" "<<v<<" "<<w<<endl;
            //cout<<f[v]<<"$$$"<<d[v]<<"$$$"<<d[u]<<"##"<<w<<endl;
            if(f[v]==0 && d[v]>d[u]+w)
            {
                d[v]=d[u]+w;
                Q.push(pii(v,d[v]));
            }
        }
        f[u]=1;
        if(u==des)
            break;

    }

}
int main()
{
    ofstream out;
    out.open("o.txt");
    ifstream in;
    in.open("A-small-attempt1.in");
    int t,n,root=1,des,u,v,w;
    in>>t;
    for(int e=1; e<=t; e++)
    {
        cout<<e<<endl;
        in>>n; //nodes
        des = n;
        int rev;
        for(int i=1; i<n; i++)
            {
                addedge(i,i+1,1);
                rev = reverse(i);
                if(rev>i && rev<=n)
                    addedge(i,rev,1);
            }
        for(int i=0; i<=n+2; i++)
            d[i]=INF;
        dijkstra(root,des);
        //for(int i=1; i<=n; i++)
          //  cout<<d[i]<<" ";
        //cout<<"%%";
        if(d[des]==INF)
            cout<<"NONE\n";
        else
        out<<"Case #"<<e<<": "<<d[des]+1<<endl;
        for(int i=0; i<n; i++)
            G[i].clear();

    }
    return 0;
}
