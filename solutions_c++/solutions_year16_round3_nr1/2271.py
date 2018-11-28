#include <bits/stdc++.h>
using namespace std;


typedef long long ll;
typedef vector <int> vi;
typedef pair< int ,int > pii;
typedef istringstream iss;
typedef ostringstream oss;
#define pb push_back
#define mp make_pair
#define f first
#define s second
#define sz size()
#define ln length()
#define rep(i,n) for(int i=0;i<n;i++)
#define fu(i,a,n) for(int i=a;i<=n;i++)
#define fd(i,n,a) for(int i=n;i>=a;i--)
#define all(a)  a.begin(),a.end() 
#define ESP (1e-9)

#define gi(n) scanf("%d",&n)
#define gl(n) cin >> n
#define pi(n) printf("%d",n)
#define pl(n) cout << n
#define ps printf(" ")
#define pn printf("\n")
#define dg(n,s); printf("%s %d",s,n)
#define imax numeric_limits<int>::max()
#define imin numeric_limits<int>::min()
#define lmax numeric_limits<ll>::max()
#define lmin numeric_limits<ll>::min()

#define mod 1000000007
#define NK 1100000
typedef pair<int ,char> pr;
int n,t;
pr a[10010];
int main(){
	freopen("A-large (2).in" , "r" , stdin);
	freopen("my25.out" , "w" , stdout);
	cin>>t;
	for(int i =1 ;i<=t;i++){
		cout<<"Case #"<<i<<": ";
		cin>>n;
		rep(i , n ){
			cin>>a[i].f;
			a[i].s = char('A' + i);
		}
	while(1){
		sort( a , a+ n);
		if(a[n-2].f > 1 && a[n-2].f == 1){
		    cout<<a[n-1].s<<" ";	
		    a[n-1].f--;
		}
		else if(a[n-1].f == 1 ){
			for(int j = n - 3 ; j >= 0 ; j--){
				if(a[j].f == 1){
					cout<<a[j].s<<" ";
				}
			}
			cout<<a[n-1].s<<a[n-2].s<<" ";
			break;
		}
		else {
			cout<<a[n-1].s<<a[n-2].s<<" ";
			a[n-1].f--;
			a[n-2].f--;
		}
	}
	cout<<"\n";
}
	return 0;
}
