#include<stdio.h>
#include<string.h>
#include<algorithm>
#include <iostream>
#include <math.h>
#include <vector>

using namespace std;

int vet[1005][1005];

unsigned long long r = 1;

int f(int n){
	if(n==0){
		return 0;
	}
	if(n==1){
		return (r+2);
	}

	return vet[r][n-1] + 2*(r+2*n-1) - 1;
}

unsigned long long g(unsigned long long k){
	//return 2*(k*(k+1) + r*(r-1));
	return k*(2*r + 2*k - 1);
}

int main()
{
	/*
	for(int i=1; i<=1000; i++){
		r = i;
		for(int j=1; j<=1000; j++){
			vet[i][j] = f(j);
		}
	}
	*/
	int n;
	unsigned long long t;

	cin>>n;
	for(int i=0; i<n; i++){
		cin>>r>>t;
		//cout<<"r = "<<r<<" t = "<<t<<endl;
	
		unsigned long long k=0;
		//int k=0;
		
		while(g(k+1) <= t){
		//	cout<<" "<<g(k+1);
			k++;
		}

		cout<<"Case #"<<i+1<<": "<<k<<endl;

	}
	
	//system("pause");
    return 0;    
}