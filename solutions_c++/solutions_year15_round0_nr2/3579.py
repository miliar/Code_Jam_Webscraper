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

int a[1200];
int big;

int main(){
	read();
	write();
	int t;
	cin >> t;
	int test = 1;
	while(t--){
		int n;
		cin >> n;
		int num;
		repi(i,0,n){
			cin >> a[i];
			big = max(big,a[i]);
		}
		int answer = big;
		repi(i,1,big+1){
			int time = i;
			repi(j,0,n){
				if(a[j] > i){
					if(a[j]%i == 0){
						time +=(a[j]/i-1);
					}
					else{
						time +=(a[j]/i);
					}
				}
			}
			answer = min(answer,time);
		}
		cout << "Case #" << test++ << ": " << answer << "\n";
	}
	return 0;
}

