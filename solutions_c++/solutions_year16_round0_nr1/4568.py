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
	//ios_base::sync_with_stdio(false) ; cin.tie(0);
    freopen("A-large.in", "r", stdin);
    freopen("large_output.txt", "w", stdout);

    int t;
    cin>>t;

    for(int test = 1 ;test <= t; test ++ )
    {
        ll n;
        cin >> n;

        if(n==0)
        {
            cout<<"Case #"<<test<<": INSOMNIA"<<endl;

        }
        else
        {

                    int flag = 0;
                    ll factor=0;
                    ll ans =0 ;

                    int mark[15];

                    for(int i=0;i<10;i++)
                    {
                        mark[i] = 0;
                    }

                    while(flag!=1)
                    {
                        factor++;
                        ll curr_value = n*factor;
                        string tmp = to_string(curr_value);

                        for(int i=0;i<tmp.size();i++)
                        {
                            mark[tmp[i]-'0'] = 1;
                        }


                        int count =0;

                        for(int i=0;i<10;i++)
                        {
                           if(mark[i] == 1)count ++;
                        }

                        if(count == 10)
                        {
                            ans = curr_value;
                            flag=1;
                        }


                    }

                    cout<<"Case #"<<test<<": "<<ans<<endl;
        }

    }

	return 0;
}
