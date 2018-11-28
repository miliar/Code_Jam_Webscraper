#include <iostream>
#include <vector>
#include <stack>
#include <cmath>
#include <queue>
#include <map>
#include <bitset>
#include <algorithm>
#include <complex>
#define Fa(i,a,v) for (int i=(a);i<= (v); i++)
#define Fba(i,a,v) for (int i=(v);i>=(a); i--)
#define F(i,v) for (int i=0;i< (v); i++)
#define Fi(i,v) for (int i=1;i<=(v); i++)
#define Fb(i,v) for (int i=(v)-1;i>=0; i--)
#define Fbi(i,v) for (int i=(v);i>0; i++)
#define pb(a) push_back((a))
#define mp(s,b) make_pair(s,b)
#define pi pair <int ,int >
#define S first
#define D second
#define ll long long
#define ld long double
#define pl pair <ll, ll>
#define pld pair <ld, ld>
using namespace std;
ll const INF = 1e18;
int main ()
{
    ios_base::sync_with_stdio(0);
    int z;
    cin>>z;
    Fi(x,z) 
    {
        int n;
        cin>>n;
        int people=0;
        int friends=0;
        string a;
        cin>>a;
        F(i,n+1)
        {	
        	char g = a[i]-'0';
        	if(people < i){
				friends +=i - people;
				people =i;
			}
        	people += g;	
		}
        cout<<"Case #"<<x<<": "<<friends<<endl;
    }
}
