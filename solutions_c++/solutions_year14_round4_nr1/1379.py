#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <utility>
#include <set>
#include <map>
#include <iostream>
#include <queue>
#include <climits>

using namespace std;

typedef long long LL;

#define PB push_back
#define FRO freopen("in.txt","r",stdin);

#define CLR(arr) memset( (arr),0,sizeof(arr) );
#define NEG(arr) memset( (arr),-1,sizeof(arr) );

#define X first
#define Y second

#define MP make_pair

#define snuke(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)


typedef pair<int,int> pint;
typedef map<int,int> mint;


#define SIZE 10100

bool vis[SIZE];
int nxt[SIZE];

int find( int x ){
    if ( x== nxt[x] )return x;
    else return nxt[x] = find( nxt[x] );
}

int v[SIZE];

bool cmp( int a,int b ){
    return a>b;
}

int main(){

    freopen("A-large.in","r",stdin);
    freopen("out.out","w",stdout);

    //FRO

    int kase;
    scanf("%d",&kase);

    for (int kk=1;kase--;++kk){

        CLR(v);

        int tmp,n,lim;
        scanf("%d %d",&n,&lim);
        for (int i=0;i<n;++i){
            scanf("%d",&tmp);
            v[i]=tmp;
        }
        sort( v,v+n,cmp );
        int ans = 0;
        CLR(vis);

        NEG(nxt);
        for (int i=0;i<=n;++i){
            nxt[i]=i;
        }

        for (int i=0;i<n;++i){
            if ( !vis[i] ){
                ans ++;
                int left = lim-v[i];
                int low = i+1,high=n-1;
                int ind = -1;
                while ( low<=high ){
                    int mid = (low+high)/2;
                    int ff= find( mid );
                    if ( v[ff]<=left ){
                        ind = ff;
                        high=mid-1;
                    }else{
                        low=mid+1;
                    }
                }
                if ( ind!= -1 && ind<n){
                    vis[ind]=true;
                    nxt[ind] = ind+1;
                }
                //cout<<v[i]<<" "<<v[ind]<<endl;
            }
        }

        printf("Case #%d: %d\n",kk,ans);

    }


    return 0;
}
