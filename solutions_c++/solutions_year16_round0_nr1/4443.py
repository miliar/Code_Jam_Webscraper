#include <bits/stdc++.h>

using namespace std;
typedef pair<double, double> pi;
typedef pair<int,pi> pii;
typedef vector<int> vi;
typedef long long ll;
typedef unsigned long long ull;
const ll MOD = 1e9 + 7;

#define MAXN 200100
#define _PI 3.14159265358979323846

bool nums[10];
void annulla(ull n)
{
	while ( n > 0)
	{
		nums[n%10] = true;
		n/= 10;
	}
}
bool ok (){ for (int i =0; i < 10; i++) if ( nums[i] == false) return false; return true;}
int main(int argc, char **argv)
{
	freopen("output.txt","w",stdout);
	freopen("input.txt","r",stdin);

	int N;
	cin>>N;
	int caseN = 1;
	while (N--)
	{
		cout<<"Case #"<<caseN++<<": ";
			ull K;
			cin>>K;
			memset(nums,0,sizeof nums);
			if ( K == 0){cout<<"INSOMNIA\n"; continue;}
			ull i = 1;
			while (!ok()){annulla(K*i); i++;}
			cout<<K*(i-1)<<"\n";
			
			
	}
	return 0;
}

