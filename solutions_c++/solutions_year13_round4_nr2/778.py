#include <string>
#include <iostream>
#include <algorithm>
#include <cstdlib>

using namespace std;

int main(){
	long long T;

	cin >> T;

	for(int t=1;t<=T;t++){
		long long N,P;
		cin >> N >> P;

		long long numTeams = 1;
		for(long long i=0;i<N;i++)
			numTeams *=2ll;

		if(P==numTeams){
			cout<<"Case #"<<t<<": "<<numTeams-1<<" "<<numTeams-1<<endl;
			continue;
		}
		long long offset = 0;
		long long blah = numTeams;
		long long ans1 = 0;
		long long blah2 = 2;
		while(P > blah/2 + offset){
			offset += blah /2;
			blah /= 2;
			ans1 += blah2;
			blah2 *= 2;
		}
		int maxLosses = 0;
		int p = P;
		while(p>1){
			p /= 2;
			maxLosses++;
		}
		int numWins = N-maxLosses;
		long long ans2 = numTeams-1;
		blah = 1;
		for(int i=0;i<numWins;i++){
			ans2 -= blah;
			blah *= 2ll;
		}

		cout<<"Case #"<<t<<": "<<ans1<<" "<<ans2<<endl;
	}

	
}