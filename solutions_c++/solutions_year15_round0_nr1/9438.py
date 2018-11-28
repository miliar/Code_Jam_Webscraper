//oggpnosn 
//hkhr 

//code jam qualification round 1 

#include<iostream>
using namespace std;

int main(){
	int T, S, i, count, j, agg;
	string input;
	cin>>T;
	for(i=0; i<T; i++){
		cin>>S>>input;
		count = 0;
		agg = input[0]-'0';
		for(j=1; j<=S; j++){
			if(agg < j)
				count += j - agg;
			agg = max(agg, j);
			agg += input[j]-'0';		
		}
		cout<<"Case #"<<i+1<<": "<<count<< "\n";
	}
	return 0;
}