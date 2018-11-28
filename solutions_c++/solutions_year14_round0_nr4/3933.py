#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <bitset>
#include <utility>
#include <ctime>
#include <cassert>
#include <climits>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<vi> vvi;
typedef pair<int,int> pii;
typedef vector<pii > vii;
typedef pair<ll,ll> pll;
typedef vector<string> vs;

#define MOD 1000000007
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define MEM(a,b) memset(a,(b),sizeof(a))
#define pr(a) cout<<#a<<" = "<<(a)<<endl
#define cin(n) int (n); scanf("%d", &(n))
#define cin2(n,m) int (n),(m); scanf("%d%d",&(n),&(m))
#define sz(a) int((a).size())
#define all(a) a.begin(),a.end()
#define loop(x,a,b) for(int (x) = (a);(x)<(b);(x)++)
#define rep(x,n)   for(int (x)=0;(x)<(n);(x)++)
#define tr(c,it) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)
#define prc(a) tr(a, it) cout<<*(it)<<" "; cout<<endl
#define pra(a,n) for(int i=0; i<(n); i++) printf("%d ",((a)[i])); printf("\n") 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define ain(a,n) int ((a)[(n)]); for(int i=0; i<(n); i++) scanf("%d",&((a)[i])) 
#define vin(a,n) vector<int> (a); (a).resize((n)); for(int i=0; i<(n); i++) scanf("%d",&((a)[i])) 

int asd[10000];

bool lol(const double &l, const double &r){
	return l>r;
}

int war(double na[],double ke[],int n){

	int k=0,flag=0,f[n],count=0;
	rep(i,n)
		f[i]=1;
	sort(na,na+n,lol);
	sort(ke,ke+n);
	rep(i,n){
		flag=0;
		rep(j,n){
			if(ke[j]>na[i]&&f[j]==1){
				f[j]=0;
				flag=1;
				count++;
				break;
			}
			
		}
		if(flag==0){
				f[k]=0;
				k++;
			}

			
	}
	
return (n-count);
}

int dwar(double na[],double ke[],int n){
	int i=0,j=0,count=0;
	sort(na,na+n);
	sort(ke,ke+n);
	while(i<n){
		if(na[i]>ke[j])
		{
			count++;
			i++;j++;
		}
		else
			i++;
		}
	return count;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,n,i,nt=0;
	cin>>t;
	while(t--){
		nt++;
		scanf("%d",&n);
		double na[n],ke[n];
		for(i=0;i<n;i++)
			cin>>na[i];
		for(i=0;i<n;i++)
			cin>>ke[i];
		printf("Case #%d: %d %d\n", nt, dwar(na,ke,n),war(na,ke,n));
	}
	return 0;
}
