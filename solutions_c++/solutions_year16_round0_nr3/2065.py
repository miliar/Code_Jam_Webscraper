#include<bits/stdc++.h>
 
using namespace std;
 
#define dbg(x) cerr << (#x) << " --> " << (x) << endl
#define lli long long int
#define pii pair<int,int>
#define mod 1000000007
#define N (int)(1e5+10)
#define mp make_pair
#define pb push_back
#define nd second
#define st first
#define endl '\n'
#define inf mod
#define sag (sol|1)
#define sol (root<<1)
#define ort ((bas+son)>>1)
#define bit(x,y) ((x>>y)&1)

int n,m,k,i,j,x,y,z;
vector<int> v;
int main(){
	n = 32;
	j = 500;

	puts("Case #1:");

	for(i=0 ; i<j; i++){
		v.clear();
		v.pb(1);
		for(k=0 ; k<n/2-1 ; k++)
			if(bit(i,k)){
				v.pb(1);
				v.pb(1);
			}
			else{
				v.pb(0);
				v.pb(0);
			}
		v.pb(1);
		for(k=0 ; k<v.size() ; k++)
			printf("%d",v[k]);
		for(k=2 ; k<=10 ; k++)
			printf(" %d",k+1);
		puts("");
	}
}
