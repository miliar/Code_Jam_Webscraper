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
typedef pair<double,double> pdd;
typedef map<int,int> mint;

void show() {cout<<'\n';}
template<typename T,typename... Args>
void show(T a, Args... args) { cout<<a<<" "; show(args...); }
template<typename T>
void show_c(T& a) { for ( auto &x:a ){ cout<<x<<" ";}cout<<endl;  }


#define SIZE 1000100

vector<int> out[SIZE];
int n,d;

LL S[SIZE];
LL AS;
LL CS;
LL RS;

LL M[SIZE];
LL AM;
LL CM;
LL RM;

pint save[SIZE];

void dfs( int x,int low,int high ){
    low = min( low,int(S[x]) );
    high = max( high,int(S[x]) );
    save[x]=MP( low,high );
    for (auto&v:out[x]){
        dfs( v,low,high );
    }
}


vector<int> min_to_max[SIZE];
vector<int> max_to_min[SIZE];

int main(){


    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.out","w",stdout);

    int kase;
    scanf("%d",&kase);

    for (int kk=1;kase--;++kk){

        for (int i=0;i<SIZE;++i){
            out[i].clear();
            min_to_max[i].clear();
            max_to_min[i].clear();
        }

        scanf("%d %d",&n,&d);
        scanf("%lld %lld %lld %lld",&S[0],&AS,&CS,&RS);
        scanf("%lld %lld %lld %lld",&M[0],&AM,&CM,&RM);
        for (int i=1;i<n;++i){
            S[i] = (S[i-1] * AS + CS)% RS;
            M[i] = (M[i-1] * AM + CM)% RM;
        }

        for (int i=1;i<n;++i){
            out[ M[i]%i ].PB( i );
        }
        dfs( 0, (1<<29),-(1<<29) );

        for (int i=0;i<n;++i){
            //show( i,save[i].X,save[i].Y );
            min_to_max[ save[i].X ].PB( save[i].Y );
            max_to_min[ save[i].Y ].PB( save[i].X );
        }

        int ans = 0;
        int cnt = 0;
        int low = max(0, int(S[0]-d) );
        int high = low+d;
        for (int i=0;i<n;++i){
            if ( low<=save[i].X && save[i].Y<=high ){
                cnt++;
            }
        }
        ans = max( ans , cnt );

        while( low+1<=S[0] ){
            for ( auto&v:min_to_max[low] ){
                if ( v<= high ){
                    cnt--;
                }
            }
            low++;
            high++;
            for ( auto&v:max_to_min[high] ){
                if ( v >= low ){
                    cnt++;
                }
            }
            ans = max( ans,cnt );
        }

        printf("Case #%d: %d\n",kk,ans);

    }


    return 0;
}
