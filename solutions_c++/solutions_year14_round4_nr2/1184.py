#include <iostream>
#include <cstdio>
#include <climits>
#include <algorithm>
#include <queue>
#include <cstring>
#include <cmath>
#include <vector>
#include <list>
#include <stack>
#include <bitset>
#include <string>
#include <cstdlib>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <deque>
#include <ctime>
#define s(n) scanf("%d",&n)
#define SET(p)      memset(p,-1,sizeof(p))
#define CLR(p)      memset(p,0,sizeof(p))
#define vi vector<int>
#define ii pair<int,int>
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define LL long long
#define ULL unsigned long long
#define R freopen("in","r",stdin)
#define W freopen("out","w",stdout)
#define imax numeric_limits<int>::max()
#define imin numeric_limits<int>::min()
#define lmax numeric_limits<ll>::max()
#define lmin numeric_limits<ll>::min()
using namespace std;


int main()
{
    R;W;
    int t,c=0;cin>>t;
    while(t--)
    {
        c++;
        printf("Case #%d: ",c);
        int n;cin>>n;
        int arr[1001],temp[1001];
        for(int i=0;i<n;i++){cin>>arr[i];temp[i]=arr[i];}
        map<int,int> my;
        for(int i=0;i<n;i++)
        {
            my[arr[i]]=i;
        }
        //sort(arr,arr+n);
        int ans=imax;
        /*for(int i=n-2;i>=0;i--)
        {
            vector<int> v;
            for(int i=0;i<n;i++)
            {
                if(my[temp[i]]>=i)v.pb(temp[i]);
            }
            
        }*/
        
        sort(temp,temp+n);
        int temp2[1001];
        int krr[1001];
        for(int i=0;i<1<<n;i++)
        {
            int a=0,b=n-1,al=0;
            int in=i;
            for(int j=0;j<n;j++)
            {
                if(in&1)
                {
                    temp2[a]=temp[al];
                    a++;al++;
                }
                else
                {
                    temp2[b]=temp[al];
                    b--;al++;
                }
                in>>=1;
            }
            for(int i=0;i<n;i++)krr[i]=arr[i];
            int hello=0;
            //cout<<"n is "<<n<<endl;
            for(int ll=n-1;ll>=0;ll--)
            {
                int o=my[temp2[ll]];
                //cout<<"o is "<<o<<endl;
                hello+=(ll-o);

                
                for(int j=o+1;j<=ll;j++)
                {
                    arr[j-1]=arr[j];
                    
                }
                arr[ll]=temp2[ll];
                for(int i=0;i<n;i++)
                {
                    my[arr[i]]=i;
                }
                
            }
            for(int i=0;i<n;i++)arr[i]=krr[i];
            for(int i=0;i<n;i++)
            {
                my[arr[i]]=i;
            }
            
            ans=min(ans,hello);
            
        }
        cout<<ans<<endl;
        
    }
}
