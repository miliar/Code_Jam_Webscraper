#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <iterator>
#include <algorithm>
#include <cmath>

using namespace std;

typedef long long LL;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<ii> vii;

#define foru(i,a,b) for(int i=int(a);i<int(b);i++)
#define forui(i,a,b,c) for(int i=int(a);i<int(b);i+=c)
#define ford(i,a,b) for(int i=int(a);i>=b;i--)

#define pb push_back
#define mp make_pair
#define f first
#define s second

#define ms(v,x) memset(v,x,sizeof v)
#define fri freopen("B-large.in","r",stdin)
#define fro freopen("B-large.out","w",stdout);

int main()
{
    fri;
    fro;
    int n;
    while(scanf("%d",&n)==1){
        cout.precision(7);
        foru(cases,1,n+1){
            double c,f,x,t,ans=0.0;
            cin>>c>>f>>x;
            t=2;
            while((ans+(x/(double)t))>(ans+(x/(double)(t+f))+(c/(double)t))){
                ans+=(c/(double)t);
                t+=f;
            }
            ans+=(x/(double)t);
            cout<<fixed<<"Case #"<<cases<<": "<<ans<<endl;
        }
    }
    return 0;
}
