#include <bits/stdc++.h>

using namespace std;

//By:-mansigupta

#define pb(x) push_back(x)

#define ll long long int

#define mp(x,y) make_pair(x,y)

#define FOR(x,y) for(x=0;x<y;x++)

#define For(x,y) for(x=1;x<=y;x++)

#define mod 1000000007

#define f first

#define s second

#define pii pair<int,int>

typedef vector <int> vi;

#define SET(x,y) memset(x,y,sizeof(x)

#define FORI(x,l,u) for(x=l;x<=u;x++)

#define PI 3.141592653589793238462643

typedef set <int> si;

typedef map <int,int> mii;

#define IT iterator

/*bool visit[];

void dfs(int u)

{

	visit[u]=1;



	int k;

	FOR(k,gr[u].size())

	{if(!visit[gr[u][k]])

	dfs(gr[u][k]);}

}*/

/*ll power(ll base, ll p)

{

    if(p==0)

    return 1;

    if(p==1)

    return (base%mod);

    base=base%mod;

    if(p%2!=0)

    {



        return((base%mod*((power((base*base)%mod,p/2)%mod)))%mod);

    }

    else

    return((power(((base%mod)*(base%mod))%mod,p/2))%mod);

}

int gc(int a,int b)

{

    if(a==0)return b;

    return gc(b%a,a);

}

*/

/*void f()

{

    priority_queue<pii,vector<pii>,greater<pii>> Q;

    Q.push({0,s});

    while(!Q.empty())

    {

        int u=Q.top().s;

        int c=Q.top().f;

        Q.pop();

        int i;

        FOR(i,g[u].size())

        {

            pii p=g[u][i];

            int v=p.s;

            int w=p.f;

            if(dist[v]>dist[u]+w){

                dist[v]=dist[u]+w;

                Q.push({dist[v],v});

            }

        }

    }

}*/



int main()

{

	//Beauty is in relaxed hard work.

	//SSGCA :)

	//Keep doing your thing, complexity would turn into simplicity! :)

    int r=1;

    int t;

    cin>>t;

    while(t--){

        int h[10]={0};

        string s;

        cin>>s;

        int i;

        int n=s.size();

        int c[27]={0};

        FOR(i,n){

           c[s[i]-'A']++;

        }

        h[0]+=c['Z'-'A'];

        c['E'-'A']-=h[0];

        c['R'-'A']-=h[0];

        c['O'-'A']-=h[0];

        c['Z'-'A']=0;

        h[6]+=c['X'-'A'];

        c['S'-'A']-=h[6];

        c['I'-'A']-=h[6];

        c['X'-'A']-=h[6];

        h[4]+=c['U'-'A'];

        c['F'-'A']-=h[4];

        c['U'-'A']-=h[4];

        c['O'-'A']-=h[4];

        c['R'-'A']-=h[4];

        h[2]+=c['W'-'A'];

        c['T'-'A']-=h[2];

        c['W'-'A']-=h[2];

        c['O'-'A']-=h[2];

        h[1]+=c['O'-'A'];

        c['O'-'A']-=h[1];

        c['N'-'A']-=h[1];

        c['E'-'A']-=h[1];

        h[5]=c['F'-'A'];

        c['F'-'A']-=h[5];

        c['I'-'A']-=h[5];

        c['V'-'A']-=h[5];

        c['E'-'A']-=h[5];

        h[3]+=c['R'-'A'];

        c['T'-'A']-=h[3];

        c['H'-'A']-=h[3];

        c['R'-'A']-=h[3];

        c['E'-'A']-=h[3];

        c['E'-'A']-=h[3];

        h[7]+=c['S'-'A'];

        c['S'-'A']-=h[7];

        c['E'-'A']-=h[7];

        c['V'-'A']-=h[7];

        c['E'-'A']-=h[7];

        c['N'-'A']-=h[7];

        h[8]+=c['H'-'A'];

        h[9]+=c['N'-'A'];

        cout<<"Case #"<<r++<<": ";

        for(i=0;i<10;i++){

            while(h[i]){cout<<i;h[i]--;}

        }

        cout<<endl;

    }

	return 0;

}
