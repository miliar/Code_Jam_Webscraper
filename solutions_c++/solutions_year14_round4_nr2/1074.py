// saurav shekhar
#include <bits/stdc++.h>

#define MOD 1000000007
#define INF 2000000000
#define EPS 1e-7
using namespace std;
typedef vector<int> vi;
typedef pair<int, int> ii;

const int LIM=1005;


int main(int argc, char* argv[])
{
	int T, qq, N, temp;
	vi A;
	scanf("%d",&T);
	for(qq=1; qq<=T; qq++) {
		A.clear();
		printf("Case #%d: ", qq);
		cin >> N;
		for(int i=0; i<N; i++) {
			cin >> temp;
			A.push_back(temp);
		}
		int ans = 0;
		for(int i=0; i<N; i++) {
			int minidx = 0;
			int mina = A[0];
			int s = A.size();
			for(int j=0; j<s; j++) {
				if(A[i] < mina) {
					minidx = j;
					mina = A[j];
				}
			}
			//printf("%d %d\n",minidx, mina );
			ans  =  ans + min(minidx , s-minidx-1);
			
			A.erase(A.begin()+minidx);
		}


		cout << ans << "\n";

		


	
		
	}
	
	
	return 0;
}
