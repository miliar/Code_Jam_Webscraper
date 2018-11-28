#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int,int > pii;
typedef pair<int,pii > piii;
//input
/*#define sc1(x) scanf("%d",&x);
#define sc2(x,y) scanf("%d%d",&x,&y);
#define sc3(x,y,z) scanf("%d%d%d",&x,&y,&z);
*/

#define sc1(x) scanf("%lld",&x);
#define sc2(x,y) scanf("%lld%lld",&x,&y);
#define sc3(x,y,z) scanf("%lld%lld%lld",&x,&y,&z);


#define pb push_back
#define mp make_pair
#define ini(x,val) memset(x,val,sizeof(x));

#define fs first
#define sc second

//some constants
#define MOD 1000000007
#define inf 99999999
#define linf 99999999999999999ll    //long long inf
#define PI 3.1415926535897932384626
const double eps=0.000000000000001 ;

#define gcd __gcd
#define tr(container, it)  for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) 
#define all(v) v.begin(),v.end()

#define debug(x) cout<<#x<<" :: "<<x<<"\n";
#define debug2(x,y) cout<<#x<<" :: "<<x<<"\t"<<#y<<" :: "<<y<<"\n";
#define debug3(x,y,z) cout<<#x<<" :: "<<x<<"\t"<<#y<<" :: "<<y<<"\t"<<#z<<" :: "<<z<<"\n";

#define LIM 100005

int hash[15];

int main(int argc, char const *argv[])
{
    ll t,i,j,ans,temp;
    
    sc1(t);
    temp = t;
    while(t--)
    {
        ll n;
        sc1(n);
        printf("Case #%lld: ",temp-t);
        if(n==0)
        {
            printf("INSOMNIA\n");
            continue;
        }
        
        ini(hash,0);
        
        for(i = 1;i<=1000000;++i)
        {
            ll temp  = i*n;
            while(temp)
            {
                hash[temp%10]++;
                temp/=10;
            }
            for(j = 0;j<10;++j)
            {
                if(!hash[j])
                {
                    break;
                }
            }
            if(j==10)
                break;
        }
        printf("%lld\n",i*n);
    }
    
    
    return 0;
}