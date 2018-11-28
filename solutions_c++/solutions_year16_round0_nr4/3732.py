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

typedef vector <ll> vi;

//set <int> ;

//map <int,int>;



/*bool visit[];

void dfs(int u)

{

	visit[u]=1;



	int k;

	FOR(k,gr[u].size())

	{if(!visit[gr[u][k]])

	dfs(gr[u][k]);}

}*/

ll power(ll base, ll p)

{

    if(p==0)

    return 1;

    if(p==1)

    return (base);

    base=base;

    if(p%2!=0)

    {



        return((base*((power((base*base),p/2)))));

    }

    else

    return((power(((base)*(base)),p/2)));

}

int main()

{

	//Beauty is in relaxed hard work.

	//SSGCA :)

	//Keep doing your thing, complexity would turn into simplicity! :)

    freopen("D-small-attempt0.in.txt","r",stdin);

    freopen("in.txt","w",stdout);

  // memset(p,1,sizeof(1));





    int t,r=0;

    cin>>t;

    while(t--)

    {

        ll k,c,s;

        cin>>k>>c>>s;

      //  cout<<k<<" "<<c;

        ll n=pow(k,c);

        vector<ll> v;

        if(k==1){

            v.pb(1);

        }else if(c==1){

            int i;

            for(i=1;i<=k;i++)v.pb(i);

            }else

            {

        ll last=0,next=1;

        v.pb(2);

        last=2;next=3;



        while(next<=k)

        {

            ll e=n/k;

            ll w=e*last;

            while(e!=k){

                e=e/k;

                w+=(e*last);

            }

            w+=last+2;

            last+=2;

            next=last+1;

            if(w>n){

                w--;

            }

            v.pb(w);

        }

        }

        int i;

        cout<<"Case #"<<++r<<": ";

        int y=sizeof(v);

        for(ll o:v)

        cout<<o<<" ";

        cout<<endl;

        v.clear();

    }

	return 0;

}
