#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#include <bits/stdc++.h>

using namespace std;
using namespace __gnu_pbds;

typedef long long LL;

typedef tree<
    int,
    null_type,
    less<int>,
    rb_tree_tag,
    tree_order_statistics_node_update>
ordered_set;
//find_by_order
//order_of_key

#define PB push_back
#define FRO freopen("in.txt","r",stdin);

#define CLR(arr) memset( (arr),0,sizeof(arr) );
#define NEG(arr) memset( (arr),-1,sizeof(arr) );
#define ALL(v) v.begin(),v.end()

#define X first
#define Y second
#define MP make_pair

typedef pair<int,int> pint;
typedef map<int,int> mint;

void show() {cout<<'\n';}
template<typename T,typename... Args>
void show(T a, Args... args) { cout<<a<<" "; show(args...); }
template<typename T>
void show_c(T& a) { for ( auto &x:a ){ cout<<x<<" ";}cout<<endl;  }


// the maximum number of vertices + 1
#define SIZE 200

// adjacency matrix (fill this up)
double cap[SIZE][SIZE];

// cost per unit of flow matrix (fill this up)
double cost[SIZE][SIZE];

// flow network and adjacency list
double fnet[SIZE][SIZE];
vector<int> out[SIZE];

// Dijkstra's successor and depth
int par[SIZE];
double d[SIZE];        // par[source] = source;

// Labelling function
double pi[SIZE];


const double INF = 1e15;
const double EPS = 1e-8;

// Dijkstra's using non-negative edge weights (cost + potential)
#define Pot(u,v) (d[u] + pi[u] - pi[v])
bool dijkstra( int n, int s, int t ){
    for( int i = 0; i < n; i++ ){
        d[i] = INF, par[i] = -1;
    }
    d[s] = 0;
    par[s] = -n - 1;

    while( 1 )
    {
        // find u with smallest d[u]
        int u = -1;
        double bestD = INF;
        for( int i = 0; i < n; i++ ) if( par[i] < 0 && d[i] < bestD )
            bestD = d[u = i];
        if(fabs( bestD -INF ) < EPS ) break;

        // relax edge (u,i) or (i,u) for all i;
        par[u] = -par[u] - 1;
        for( int i = 0; i < out[u].size(); i++ )
        {
            // try undoing edge v->u
            int v = out[u][i];
            if( par[v] >= 0 ) continue;
            if( fnet[v][u] && d[v] > Pot(u,v) - cost[v][u] )
                d[v] = Pot( u, v ) - cost[v][u], par[v] = -u-1;

            // try edge u->v
            if( fnet[u][v] < cap[u][v] && d[v] > Pot(u,v) + cost[u][v] )
                d[v] = Pot(u,v) + cost[u][v], par[v] = -u - 1;
        }
    }

    for( int i = 0; i < n; i++ ) if( pi[i] < INF ) pi[i] += d[i];

    return par[t] >= 0;
}
#undef Pot

double mincost( int n, int s, int t, double &fcost)
{
    //clear the vector
    for (int i=0;i<n;++i){
        out[i].clear();
    }

    // build the adjacency list
    for( int i = 0; i < n; i++ )
        for( int j = 0; j < n; j++ )
            if( cap[i][j] >0 || cap[j][i] >0 ) out[i].PB(j);


    for (int i=0;i<SIZE;++i){
        for (int j=0;j<SIZE;++j){
            fnet[i][j] = 0;
        }
        pi[i] = 0;
    }

    double flow = fcost = 0;

    // repeatedly, find a cheapest path from s to t
    while( dijkstra( n, s, t ) )
    {
        // get the bottleneck capacity
        double bot = INF;
        for( int v = t, u = par[v]; v != s; u = par[v = u] )
            bot =min(bot, fnet[v][u] ? fnet[v][u] : ( cap[u][v] - fnet[u][v] ) );

        // update the flow network
        for( int v = t, u = par[v]; v != s ; u = par[v = u] )
            if( fnet[v][u] ) { fnet[v][u] -= bot; fcost -=bot * cost[v][u]; }
            else { fnet[u][v] += bot; fcost += bot * cost[u][v]; }

        flow += bot;
    }
    return flow;
}


double R[SIZE];
double C[SIZE];
int n;
double V,X;


void build( double time ,bool neg){

    for (int i=0;i<SIZE;++i){
        for (int j=0;j<SIZE;++j){
            cap[i][j] = 0;
            cost[i][j] = 0;
        }
    }

    int source = 0,sink = n+2;
    for (int i=1;i<=n;++i){
        cap[source][i] = time*R[i];
        cost[source][i] = C[i]-X;

        if ( neg ){
            cost[source][i] = -cost[source][i];
        }

        cap[i][n+1] = INF;
        cost[i][n+1] = 0;
    }
    cap[n+1][sink] = V;
    cost[n+1][sink] = 0;
}

int main(){

    freopen("B-large.in","r",stdin);
    freopen("out.out","w",stdout);

    int kase;
    scanf("%d",&kase);

    for (int kk=1;kase--;++kk){


        cin>>n;
        cin>>V>>X;

        for (int i=1;i<=n;++i){
            cin>>R[i];
            cin>>C[i];
        }


        double low = 0,high = 1e15;
        double ans = -1;
        while ( low<high ){

            double mid = (low+high)/2;
            build(mid,0);
            double cc1,flow1;
            flow1= mincost( n+3,0,n+2,cc1 );

            build(mid,1);
            double cc2,flow2;
            flow2= mincost( n+3,0,n+2,cc2 );
            cc2 = -cc2;
            if ( fabs( flow1-V )<EPS && fabs( flow2-V )<EPS && min( cc1 ,cc2 )<=0 && max( cc1,cc2 ) >=0  ){
                ans = mid;
                high = mid-EPS;
            }else{
                low = mid+EPS;
            }

        }
        ans += EPS;
        if ( ans < 0 ){
            printf("Case #%d: IMPOSSIBLE\n",kk);
        }else{
            printf("Case #%d: %.8f\n",kk,ans);
        }

    }

    return 0;
}
