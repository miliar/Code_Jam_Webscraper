#include <iostream>
#include <stdlib.h>
#include <math.h>

using namespace std;

bool *digitsFound(long long N){
	bool *digitsPresent = new bool[10];
	int i;
	for(i = 0 ; i < 10 ; i++)
		digitsPresent[i] = false;
	while(N > 0){
		digitsPresent[N%10] = true;
		N = N/10;
	}	
	return digitsPresent;
}

int main(){
	int i,j,k,l;
	int T, flag;
	long long N;
	bool digitsPresent[10], *digitsPresentInThisNum;

	cin>>T;
	for(l = 0 ; l < T ; l++){
		cout<<"Case #"<<l+1<<": ";
		cin>>N;
		long long initNum = N;
		if(N == 0){
			cout<<"INSOMNIA\n";
			continue;
		}
		for(i = 0 ; i < 10 ; i++)
			digitsPresent[i] = false;
		while(true){
			digitsPresentInThisNum = digitsFound(N);
			for(i = 0 ; i < 10 ; i++)
				digitsPresent[i] = digitsPresent[i] | digitsPresentInThisNum[i];
			for(i = 0 ; i < 10 ; i++)
				if(!digitsPresent[i])
					break;
			if(i == 10)
			{
				cout<<N<<"\n";
				break;
			}
			N = N + initNum;		
			delete[] digitsPresentInThisNum;
		}
	}
	return 0;
}
