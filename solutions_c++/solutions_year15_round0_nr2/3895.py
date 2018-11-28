#include <iostream>
#include <stdlib.h>
#include <cmath>
#include <algorithm>

#define maxcakes 1000

using namespace std;

int getMinimum(int *A, int D){
	int *B = new int[D+1];
	int i;

	for(i = 0 ; i < D ; i++)
		B[i] = A[i];

	sort(B, B+D);
	int minimum = B[D-1];
	//cout<<minimum<<"\t";
	if(minimum <= 3){
		delete B;
		return minimum;
	}

	int maximum = B[D-1];

	for(i = 2 ; i <= maximum/2 ; i++)
	{
		B[D] = i;
		B[D-1] = maximum - i;
		minimum = min(minimum, getMinimum(B, D+1) + 1);
	}

	delete B;
	return minimum;
}

int main(){
	int i,j,k;
	int T, D;
	int *A;
	cin>>T;
	for(i = 0 ; i < T ; i++){
		cin>>D;
		A = new int[D];
		for(j = 0 ; j < D ; j++)
			cin>>A[j];
		int minimum = getMinimum(A, D);
		delete A;
		cout<<"Case #"<<i+1<<": "<<minimum<<"\n";
	}
}
