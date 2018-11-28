#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<algorithm>
#include<queue>
#include<stack>
#include<cmath>
#include<string.h>
#include<string>
using namespace std;

vector< pair<int,int> > v;
const long long m = 1000002013LL;
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("paout.txt","w",stdout);

    int T,N,M,tmp;
    long long ini,cha;
    int a,b,c;

    scanf(" %d",&T);

    for( int cas = 1; cas <= T; cas++ ){
        scanf("%d %d",&N,&M);
        v.clear();
        cha = ini = 0LL;
        while( M-- ){
            scanf(" %d %d %d",&a,&b,&c);
            ini = (ini+c*(b-a)*(N+N-(b-a)+1)/2) % m;
            while( c-- )
                v.push_back(pair<int,int>(a,b));
        }
        sort(v.begin(),v.end());
        for( int i = 0; i < v.size(); i++ ){
            for( int j = i+1; j < v.size(); j++ ){
                if( v[i].second >= v[j].first ){
                    tmp = max(v[i].second,v[j].second);
                    v[j].second = min(v[i].second,v[j].second);
                    v[i].second = tmp;
                }else{
                    break;
                }
            }
            a = v[i].first;
            b = v[i].second;
            cha = (cha+(b-a)*(N+N-(b-a)+1)/2) % m;
        }
        printf("Case #%d: %lld\n",cas,(ini-cha+m)%m);
    }




    return 0;
}
