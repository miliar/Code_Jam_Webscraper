#include <vector>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include<iomanip>
using namespace std;

typedef long long ll;
typedef vector <int> vi;
typedef pair< int ,int > pii;
#define pb push_back
#define sz size()
#define ln length()
#define fore(i,a,b) for(int i=a;i<b;i++)
#define fores(i,a,b) for(int i=a;i<=b;i++)
#define ford(i,a,b) for(int i=a;i>=b;i--)
#define all(a) a.begin(),a.end()
#define mp make_pair
#define ff first
#define ss second
#define sc(a) scanf("%d",&a)
#define md 1000000007

string num(ll n)
{
    string ans = "";
    while(n!=0) {
        int dig = n%10;
        ans+=(char)('0' + dig);
        n/=10;
    }
    reverse(all(ans));
    return ans;
}
int main() {
	freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	fore(z,0,t)
	{
		printf("Case #%d: ",z+1);
		ll n;
		cin>>n;
		if(n == 0) {
            cout<<"INSOMNIA"<<endl;
		}
		else {
            vi vis(10,0);
            ll nos = n;
            while(true) {
                string tr = num(nos);
                fore(i,0,tr.sz) {
                    vis[tr[i]-'0']++;
                }
                bool found = false;
                fore(i,0,10) {
                    if(!vis[i]) {
                        found = true;
                        break;
                    }
                }
                if(!found) {
                    cout<<nos<<endl;
                    break;
                }
                nos+=n;
            }
		}
	}
	return 0;
}
