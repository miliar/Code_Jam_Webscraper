# include <bits/stdc++.h>

using namespace std;

# define mp make_pair
# define pb push_back
# define repi(i,p,q) for(int i=p;i<q;i++)
# define repd(i,p,q) for(int i=p;i>=q;i--)
# define sz(x) x.size()
# define INF 2000000000
# define mod 1000003

typedef map<int,int> MI;
typedef pair<int,int> PI;
typedef long long int LLI;
typedef long int LI;
typedef int I;

#define read() freopen("input.txt", "r", stdin)
#define write() freopen("output.txt", "w", stdout)

string a;

int main(){
	read();
	write();
	int t;
	cin >> t;
	int test = 1;
	while(t--){
		int shyness;
		cin >> shyness;
		cin >> a;
		int total = 0;
		int extra = 0;
		total = total + (a[0]-'0');
		repi(i,1,a.length()){
			if(i > total){
				extra = extra + (i-total);
				total = total + (i-total);
			}
			total = total + (a[i]-'0');
		}
		cout << "Case #" << test++ << ": " << extra << "\n";
	}
	return 0;
}

