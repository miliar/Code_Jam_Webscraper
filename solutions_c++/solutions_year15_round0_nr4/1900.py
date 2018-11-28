#include <cstdio>
#include <iostream>
#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <functional> 
#include <string>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <bitset>
#include <numeric>
#include <cstring>
//#include <deque>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef map<int,int> mii;
typedef vector<int> vi;
typedef vector< vector<int> > vvi;
typedef vector<char> vc;
typedef vector<bool> vb;
typedef vector<string> vs;

#define rep(i,n) for(int i=0;i<n;i++)
#define forup(i,a,b) for(int i=a;i<=b;i++)
#define fordn(i,a,b) for(int i=a;i>=b;i--)
#define drep(i,n) for(i=0;i<n;i++)
#define dforup(i,a,b) for(i=a;i<=b;i++)
#define dfordn(i,a,b) for(i=a;i>=b;i--)
#define all(x) x.begin(),x.end()
#define permute(x) next_permutation(all(x))
#define ri(x) scanf("%d",&x)
#define rl(x) scanf("%lld",&x)
#define rd(x) scanf("%lf",&x);
#define rs(x) scanf(" %s",x);
#define pb push_back
#define mp make_pair
#define fi first
#define sc second
#define MOD 1000000007

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
    int t,x,r,c,mul;
    cin>>t;
    int k=0;
    while(t-->0)
    {
    	k++;
        cin>>x>>r>>c;
        mul=r*c;
        if(x == 1)
                cout<<"Case #"<<k<<": "<<"GABRIEL"<<endl;
        else if(x == 2)
        {
        	if(mul%2 == 0)
        	cout<<"Case #"<<k<<": "<<"GABRIEL"<<endl;
        	else
        	cout<<"Case #"<<k<<": "<<"RICHARD"<<endl;
        }
        else if(x == 3)
        {
        	if(mul == 6 || mul == 9 || mul == 12)
        	cout<<"Case #"<<k<<": "<<"GABRIEL"<<endl;
        	else
        	cout<<"Case #"<<k<<": "<<"RICHARD"<<endl;
        }
        else
        {
        	if(mul ==12 || mul == 16)
        	cout<<"Case #"<<k<<": "<<"GABRIEL"<<endl;
        	else
        	cout<<"Case #"<<k<<": "<<"RICHARD"<<endl;
        }
    }
    return 0;
}

