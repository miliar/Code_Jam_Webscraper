#define LOCAL
#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>
#include<iostream>
#include <algorithm>

using namespace std;


int find(int N,int target){
	int count = 1;
	while (true)
	{
		int k = count*N;
		while (k > 0){
			if (k % 10 == target){
				//cout << target << " " << count*N << endl;
				return count*N;
			}
			k = k / 10;

		}
			count++;
	}

	return 0;
}


int main(){
	std::ios_base::sync_with_stdio(false);

#ifdef LOCAL
	freopen("A-large.in", "r", stdin);
	freopen("result.in", "w", stdout);
#endif
	int M;
	scanf("%d",&M);
	for (int i = 1; i <= M; i++){
		int N;
		int res = 0;
		scanf("%d", &N);

		if (N == 0){
			cout << "Case #" << i << ": INSOMNIA" << endl;
		}
		else{
			for (int j = 0; j < 10; j++){
				res = max(res, find(N, j));
			}

			cout << "Case #" << i << ": "<<res<<endl;
		}

	 }

	return 0;

}