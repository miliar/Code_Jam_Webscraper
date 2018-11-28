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
#define vs vector<string>
using namespace std;


int main()
{
    R;W;
    int t,c=0;cin>>t;
    while(t--)
    {
        c++;
        printf("Case #%d: ",c);
        int m,n;
        cin>>m>>n;
        vs inp(m);
        for(int i=0;i<m;i++)cin>>inp[i];
        int ans=-1,index=-1;
        int limit=1;
        for(int i=0;i<m;i++)limit*=n;
        for(int i=0;i<limit;i++)
        {
            int in=i;
            set<string> arr[4];
            for(int j=0;j<m;j++)
            {
                int a=in%n;
                in/=n;
                arr[a].insert(inp[j]);
            }
            /*for(int i=0;i<n;i++)
            {
                for(string k: arr[i])
                {
                    cout<<k<<" ";
                    
                }
                cout<<"____________";
                cout<<endl;
            }*/
            bool flag=0;
            for(int i=0;i<n;i++)
            {
                if(arr[i].size()==0)flag=1;
            }
            if(flag){continue;}
            int temp=0;
            set<string> he;
            for(int k=0;k<n;k++)
            {
                for(string l: arr[k])
                {
                    for(int len=0;len<=l.size();len++)
                    {
                        he.insert(l.substr(0,len));
                    }
                }
                temp+=he.size();
                he.clear();
            }
            
            if(temp==ans)
            {
                index++;
            }
            else
            {
                if(temp>ans)
                {
                    ans=temp;
                    index=1;
                }
            }
            
        }
        cout<<ans<<" "<<index<<endl;
    }
}
