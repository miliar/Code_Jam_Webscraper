#include <bits/stdc++.h>
using namespace std;

#define whatis(x) cout << #x << " is " << x << endl;

#define MAX 1000001
#define MOD 1000000007
#define INF 1e18
#define PI 3.14159265359

#define STDSYNC std::ios::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)
#define swap(VAR1,VAR2) VAR1=VAR1^VAR2;VAR2=VAR1^VAR2;VAR1=VAR1^VAR2

typedef long long int ll;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map<int,int> mii;
typedef map<string,int> msi;
typedef priority_queue < ll , vector < ll > , greater < ll > > minheap;
typedef priority_queue < ll , vector < ll > , less < ll > > maxheap;

int main()
{
	STDSYNC;
	ll t,a,b,c,i,j,k,n,m;
    cin >> t;
    for(i=0;i<t;i++){
        cin >> n;
        if(n==0){
            cout << "Case #" << (i+1) << ": INSOMNIA"  << endl;
        }
        else{
        ll visited[10];
        ll rem = 10;
        for(j=0;j<10;j++){
            visited[j] = 0;
        }
        ll cur=n,temp = n, ans=0;
        while(rem>0){
            temp = cur;
            while(temp){
                if(visited[temp%10]==0){
                    visited[temp%10]=1;
                    rem-=1;
                }
                temp/=10;
            }
            if(rem == 0)
                ans=cur;
            cur+=n;
        }
        cout << "Case #" << (i+1) << ": " << ans << endl;
        }
    }
	return 0;
}
