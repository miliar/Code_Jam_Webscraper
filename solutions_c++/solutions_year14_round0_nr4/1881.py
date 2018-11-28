#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
using namespace std;
int ana(vector<double>&A,vector<double>&B){
	int M = A.size(), N=B.size();
	int i=0,j=0,ans=0;
	while(i<M && j<N){
		while(i<M && A[i]<B[j])++i;
		if(i<M){
			++ans;
			++j;++i;
		}
	}
	return ans;
}
int main(){
	int T;cin>>T;
	int idx =0 ;
	vector<double> A;
	vector<double> B;
	while(T--){
		++idx;
		int N;cin>>N;
		A.resize(N);
		B.resize(N);
		for(int i=0;i<N;++i)
			cin >> A[i];
		for(int i=0;i<N;++i)
			cin >> B[i];
		sort(A.begin(),A.end());
		sort(B.begin(),B.end());
		cout << "Case #"<<idx<<": "<<ana(A,B)<<" "<<(N-ana(B,A)) << endl;
	}
	return 0;
}
