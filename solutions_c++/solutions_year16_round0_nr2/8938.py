#include <bits/stdc++.h>

#define read() freopen("input.txt", "r", stdin)
#define write() freopen("output.txt", "w", stdout)

using namespace std;

# define mp make_pair
# define pb push_back
# define repi(i,p,q) for(long i=p;i<q;i++)
# define repd(i,p,q) for(long i=p;i>=q;i--)
# define sz(x) x.size()
# define INF 2000000000
# define MOD 1000000007

typedef map<int,int> MI;
typedef pair<int,int> PI;
typedef long long int LLI;
typedef long int LI;
typedef int I;

int main(){
	//dear god
	read();
	write();
	int t;
	cin >> t;
	int test = 1;
	while(t--){
		string a;
		cin >> a;
		int counter = 0;
		repi(i,1,a.length()){
			if(a[i] != a[i-1]){
				counter++;
			}
		}
		if(a[a.length()-1] == '-'){
			counter++;
		}
		cout << "Case #" << test << ": " << counter << "\n";
		test++;
	}
    return 0;
}

