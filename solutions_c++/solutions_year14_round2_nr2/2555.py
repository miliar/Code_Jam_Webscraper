#include<iostream>
#include<cstdlib>
#include<cmath>
#include<stdio.h>
#include<algorithm>

using namespace std;


int main(){

	int T;
	cin>>T;
	for(int i=1;i<=T;i++){
		int A,B,K;
		cin>>A>>B>>K;
		int count = 0;
		for(int j=0;j<A;j++){
			for(int k=0;k<B;k++){
				int value = j & k;
				if(value < K)
					count++;
			}
		}
		cout<<"Case #"<<i<<": "<<count<<endl;
	}
}
