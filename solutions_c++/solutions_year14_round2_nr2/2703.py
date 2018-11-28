#include <bits/stdc++.h>
#define reset ios_base::sync_with_stdio(false);cin.tie(0);

using namespace std;


int main(){	reset

	long long int t; cin>>t;
	for(long long int i=0; i<t; i++){
		cout<<"Case #"<<i+1<<": ";
		long long int A, B, K, ways=0, c=0; cin>>A>>B>>K;
		for(long long int j=0; j<A; j++)
			for(long long int k=0; k<B; k++){
				c = j & k;
				if(c<K)
					ways++;
			}
		cout<<ways<<"\n";			

	}

	return 0;
}