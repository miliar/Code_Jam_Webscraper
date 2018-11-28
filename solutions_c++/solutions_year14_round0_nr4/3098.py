#include<cstdio>
#include<iostream>
#include<iomanip>
#include<cmath>
#include<cstring>
#include<cstdlib>
#include<string>
#include<sstream>
#include<vector>
#include<map>
#include<set>
#include<bitset>
#include<algorithm>
#include<cassert>
#include<ctime>
#include<queue>
using namespace std;
#define LARGE

int nocheat(vector<double> &A,vector<double> &B, int N){
	int indA = 0, indB = 0;
	while(indA < N && indB < N){
		if(A[indA] < B[indB]){
			++indA;
			++indB;
		}
		else{
			++indB;
		}
	}

	return (N - indA);
}

int cheat(vector<double> &A,vector<double> &B, int N){
	int indA = N-1; 
	int indB = N-1;
	while(indA >= 0 && indB >= 0){
		if(A[indA] > B[indB]){
			--indA;
			--indB;
		}
		else{
			--indB;
		}
	}

	return (N - indA-1);
}

int main()
{
#ifdef SMALL
	freopen("D-small-attempt0.in","rt",stdin);
	freopen("D-small-attempt0.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("D-large.in","rt",stdin);
	freopen("D-large-attempt0.out","wt",stdout);
#endif
	int T,N;
	scanf("%d", &T);
	for(int t=1; t<=T; t++)
	{
		scanf("%d", &N);
		vector<double> A,B;
		double temp;
		for(int i = 0; i < N; i++){
			cin >> temp;
			A.push_back(temp);
		}
		for(int i = 0; i < N; i++){
			cin >> temp;
			B.push_back(temp);
		}

		printf("Case #%d: ", t);
		sort(A.begin(),A.end());
		sort(B.begin(),B.end());
		int result_nocheat = nocheat(A,B,N);
		int result_cheat = cheat(A,B,N);

		cout << result_cheat << " " << result_nocheat <<endl;
	}
}
