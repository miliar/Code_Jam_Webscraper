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

}*/

int gc(int a,int b)

{

    if(a==0)return b;

    return gc(b%a,a);

}

int main()

{

	//Beauty is in relaxed hard work.

	//SSGCA :)

	//Keep doing your thing, complexity would turn into simplicity! :)

    freopen("B-large.in.txt","r",stdin);

   freopen("in.txt","w",stdout);

    int t,r=0;

    cin>>t;

    while(t--)

    {

        string s;

        cin>>s;

        string q="";

        int n=s.size();

        int i=0;

        while(i<n)

        {

            if(s[i]=='+'){

                q+="+";

                while(i<n && s[i]=='+')i++;

            }else{

                q+="-";

                while(i<n && s[i]=='-')i++;

            }

        }

        //cout<<q;

        int l=q.size();

        int ans=0;

        if(q[l-1]=='-'){

            ans=l;

        }else{

            ans=l-1;

        }

        cout<<"Case #"<<++r<<": "<<ans<<endl;

    }

	return 0;

}
