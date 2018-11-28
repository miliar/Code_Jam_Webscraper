#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int dp[1010][1010];
int num[1010];

void init() 
{
	int ans;
	for (int i = 1; i<=1000; i++) {
		for (int j = 1 ; j<=i; j++) {
			ans = i/j;
			if(i%j == 0)
				ans--;
			dp[i][j] = ans;
		}
	}
}

void dd(int n){
	cout << n << endl;
}
int main() 
{
	int T,D,n;
	while(cin >> T) {
		init();
		for (int cas = 1; cas<=T; cas++) {
			cout<< "Case #"<<cas<<": ";
			int maxx = -1,ans =(1<<20),tmp;
			cin >> D;
			for (int i = 0; i<D; i++) {
				cin >> num[i];
				if (num[i] > maxx)
					maxx = num[i];
			}
			for(int i = 1 , j; i<=maxx; i++) {
				tmp = 0;
				for (j = 0; j<D; j++) {
					tmp+=dp[num[j]][i];
					//dd(dp[num[j]][i]);
				}
				//cout << endl;
				tmp+=i;
				ans = ans<tmp?ans:tmp;
			}
			cout<<ans<<endl;
		}
	}
	return 0;
}
