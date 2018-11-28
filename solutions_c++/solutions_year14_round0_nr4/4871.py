#include <iostream>
#include <algorithm>
using namespace std;
 
int main() {
	int T, n, i, j, countWar, countDeceitfulWar;
	float blockNaomi[1000], blockKen[1000];
	cin>>T;
	for(int testCase=1;testCase<=T;++testCase){
		cin>>n;
		for(i=0;i<n;++i) cin>>blockNaomi[i];
		for(i=0;i<n;++i) cin>>blockKen[i];
		sort(blockNaomi,blockNaomi+n);
		sort(blockKen,blockKen+n);
		i=0,j=0;
		countDeceitfulWar=0;
		while(i<n){
			if(blockNaomi[i]>blockKen[j]){
				j++;
				countDeceitfulWar++;
			}
			i++;
		}
		i=0,j=0;
		countWar=0;
		while(i<n){
			if(j==n) break;
			if(blockNaomi[i]<blockKen[j]){
				countWar--;
				i++;
			}
			j++;
		}
		countWar+=n;
		cout<<"Case #"<<testCase<<": "<<countDeceitfulWar<<" "<<countWar<<endl;
	}
	return 0;
}