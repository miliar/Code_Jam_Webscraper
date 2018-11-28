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
		long long n;
		cin >> n;
		if(n == 0){
			cout << "Case #" << test << ": " << "INSOMNIA\n";
		}
		else{
			int a[12] = {0};
			int mult = 0;
			while(1){
				int flag = 0;
				repi(i,0,10){
					if(a[i] == 0){
						flag = 1;
					}
				}
				if(flag == 1){
					mult++;
					long long temp = mult*n;
					while(temp != 0){
						a[temp%10]++;
						temp = temp/10;
					}
				}
				else{
					cout << "Case #" << test << ": " << mult*n << "\n";
					break;
				}
			}
		}
		test++;
	}
    return 0;
}

