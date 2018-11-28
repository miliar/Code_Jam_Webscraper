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

vector <string> ans ;

int total=0;

ll mark[16][16];

void precompute()
{
    for(int i=2;i<=10;i++)
    {
        mark[i][0]=1;
        for(int j=1;j<=15;j++)
        {
            mark[i][j] = mark[i][j-1] * i ; 

        }
    }
}

bool check_base(ll val,ll bas)
{

    for(int i=15;i>=0;i--)
    {

        if(mark[bas][i]<=val)
            val = val - mark[bas][i];

        if(val==0)
            return true;
        

    }


    return false;
}



ll not_prime (ll n,ll base)
{
    if(n==2||n==3||n==5)
        return -1;
    for(int i=2; i <= sqrt(n) ;i++)
    {
        if(n%i==0)
        {

            if(check_base(i,base))
            return i;

        }
    }

    return -1;

}

ll solve(string temp, int base)
{

   ll value=0;

   ll x = 1;
   value += (temp[15]-'0') * x;
   for(int i=14; i>=0; i--)
   {
     x*=base;
     value += (temp[i]-'0') * x;  
   }

    return not_prime(value,base); 
    
}


void compute(string s,int len)
{
    if(len == 16)
    {

        if(total == 50)
            return;

        int count = 0;
        //cout<<s<<endl;
        vector<ll> v;
        for(int i=2;i<=10;i++)
        {
            ll xxxx = solve(s,i);
            v.push_back(xxxx);
            if(xxxx!=-1)
                count ++;
        }

        if(count == 9)
        {
            //ans.push_back(s);
            cout<<s<<" ";
            for(int i=0;i<v.size();i++)
            {
                if(i==8)
                cout<<v[i];
                else
                cout<<v[i]<<" ";
            }
            cout<<endl;
            total++;

        }

    }
    else if(len==15)
    {
        string xx=s;
        xx.push_back('1');
        compute(xx,len+1);
    }
    else
    {
        string yy=s;
        yy.push_back('0');
        compute(yy,len+1);
        string xx=s;
        xx.push_back('1');
        compute(xx,len+1);
    }
}


int main()
{
	//ios_base::sync_with_stdio(false) ; cin.tie(0);
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("Cout.txt", "w", stdout);

    precompute();

    int t;
    cin>>t;

    for(int test = 1 ;test <= t; test ++ )
    {
        int n,j;
        cin>>n>>j;
        cout<<"Case #"<<test<<":"<<endl;

        string s;
        s.push_back('1');
        string xx=s;
        xx.push_back('0');
        compute(xx,2);
        string yy=s;
        yy.push_back('1');
        compute(yy,2);

        //cout<<ans.size()<<endl;
       /* for(int i=0;ans.size();i++)
        {
            cout<<ans[i]<<endl;
        }
        */
        //cout<<"Case #"<<test<<": "<<ans<<endl;

    }

	return 0;
}
