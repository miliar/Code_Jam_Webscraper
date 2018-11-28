#include <iostream>
#include <algorithm>
using namespace std;

int main(){
	double A[1001],B[1001];

	int T;
	cin>>T;
	int N;
	for(int cc=1;cc<=T;++cc){
		printf("Case #%d: ", cc);

		cin>>N;
		for(int i=0;i<N;++i){
			cin>>A[i];
		}
		for(int i=0;i<N;++i){
			cin>>B[i];
		}
		int X,Y;
		sort(A,A+N);
		sort(B,B+N);

		int j=0;
		Y=0;
		for(int i=0;i<N;++i){
			while(j<N && B[j]<A[i]){
				++Y;
				++j;
			}
			++j;
		}
		
		j = 0;
		X=0;
		for(int i=0;i<N;++i){
			if(A[i]<B[j]){
				
			} else {
				++j;
				++X;
			}
		}

		printf("%d %d\n", X, Y);
	}
}