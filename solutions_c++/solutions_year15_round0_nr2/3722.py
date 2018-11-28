#include <iostream>
#include <cmath>

using namespace std;

#define MAXN 10010

int cakes[MAXN];

int main()
{
	int T,N,res,mx,cur;
	cin >> T;
	for(int k=1;k<=T;k++){
		scanf(" %d",&N);
		res = 1e9; mx=cur=0;
		for(int i=0;i<N;i++)
		{
			cin >> cakes[i];
			mx=max(mx,cakes[i]);
		}
		for(int i=1;i<=mx;i++){
			cur = 0;
			for(int j=0;j<N;j++)
				cur += (cakes[j]-1) / i;
			res = min(res,cur+i);
		}
		cout << "Case #" << k << ": " << res << endl;
	}
	return 0;
}

