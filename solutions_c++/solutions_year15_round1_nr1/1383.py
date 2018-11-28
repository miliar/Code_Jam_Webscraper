#include <iostream>
#include <iomanip>
#include <cmath>
#include <algorithm>

using namespace std;

int main(){
	int i,j,k,l;
	int N,T;
	cin>>T;
	long long *A;
	for(l = 0 ; l < T ; l++){
		cin>>N;
		A = new long long[N];
		for(i = 0 ; i < N ; i++)
			cin>>A[i];
		cout<<"Case #"<<l+1<<": ";
		long long count = 0;
		for(i = 1 ; i < N ; i++)
			if(A[i] < A[i-1])
				count+=A[i-1] - A[i];
		cout<<count<<" ";
		count = 0;
		long long maxP = 0;
		for(i = 1 ; i < N ; i++)
			maxP = max(maxP, A[i-1]-A[i]);
		for(i = 0 ; i < N -1 ; i++)
			count+=min(A[i], maxP);
		cout<<count<<"\n";
	}
	return 0;
}