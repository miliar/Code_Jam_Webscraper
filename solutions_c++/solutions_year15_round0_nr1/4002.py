#include <iostream>
#include <algorithm>
#include <string>
#include <stdlib.h>

using namespace std;

int main(){
	int i,j,k;
	int T, N;
	int *S;
	string info;
	cin>>T;
	for(i = 0 ; i < T ; i++){
		cin>>N;
		S = new int[N+1];
		cin>>info;
		for(j = 0 ; j <= N ; j++){
			S[j] = info[j] - '0';
		}
		int count = 0;
		int total=0;
		for(j = 0 ; j <= N ; j++){
			if(S[j] == 0)
				continue;
			if(count < j){
				total += j - count;
				count = j + S[j];
			}
			else
				count = count + S[j];
		}
		
		S[0] += total;
		count=0;
		for(j = 0 ; j <= N ; j++){
			if(S[j] == 0)
				continue;
			if(count < j){
				cout<<"Code Fucked Up in casecccccc\t"<<i<<"\n";
				exit(0);
			}
			else
				count = count + S[j];
		}

		S[0] -= total;
		if(total != 0)
			S[0] = S[0] + total -1;
		count=0;
		for(j = 0 ; j <= N ; j++){
			if(S[j] == 0)
				continue;
			if(count < j){
				break;
			}
			else
				count = count + S[j];
		}

		if(j == N+1 && total != 0){
			cout<<"Code Fucked up in\t"<<i<<"\n";
			exit(0);
		}

		cout<<"Case #"<<i+1<<": "<<total<<"\n";
		delete S;
	}
	return 0;
}