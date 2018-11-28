/* Code and Temmplate by sumit.asr@gmail.com */

#include <iostream>
#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory.h>
#include <string>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vll;
typedef vector<vll> vvll;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef double ld;
typedef vector<ld> vld;

#define pb push_back
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define rep(i, n) for(int i = 0; i < (int)(n); i++) //int ascending
#define repc(i, a, n) for(int i = (int)(a); i < (int)(n); i++) //customized
#define repd(i, n) for(int i = (int)(n) - 1; i >= 0; i--) //int descending
#define repl(i,n)   for(ll i=0;i<n;i++)

#define mp make_pair
#define fs first
#define sc second
#define last(a) int(a.size() - 1)

#define MEM(a,b)      memset(a,(b),sizeof(a))  //memset(arr,0,sizeof(arr))
#define MOD           1000000007


int main()
{
	ios_base::sync_with_stdio(false) ; cin.tie(0);
    freopen("b.in", "r", stdin);
    freopen("outb.in", "w", stdout);

    int t;
    cin>>t;

    int ans=0;

    for(int test = 1 ;test <= t; test ++ )
    {
        
            int n;
            cin >> n;

            int sum = 0; 
            std::vector< pair <int,char> > v;
            for(int i=0;i<n;i++)
            {
                int x;    
                cin>>x;

                v.pb(mp(x,'A'+i));

                sum += x;

            }

            cout<<"Case #"<<test<<": ";


            sort(v.begin(),v.end());
            /*
            for(int i=0;i<n;i++)
            {
                cout<<v[i].first <<"  "<<v[i].second <<endl;
            }
            */

            if(n==2)
            {
                if(v[0].first==v[1].first)
                {
                    for(int i=0;i<v[0].first;i++)
                    {
                        cout<<"AB";
                        if(i<v[0].first-1)
                            cout<<" ";
                    }
                    cout<<endl;
                }
            }
            else
            {
            while(sum!=0)
            {
                    if(sum==2)
                    {
                        cout<<v[n-1].second<<v[n-2].second<<endl;
                        sum=sum-2;
                        break; 
                    }

                    double temp = ((double)(v[n-1].first-1)*(double)100)/(double)(sum-1) ;
                    if(temp>50.0)
                    {

                    }

                    //cout<<v[n-1].first << "   "<< sum <<  " "<< ((v[n-1].first)*100)/sum <<endl;
                    cout<<v[n-1].second<<" ";
                    v[n-1].first--;
                    sum--;

                    sort(v.begin(),v.end());


            }
            }

                    
        

    }

	return 0;
}
