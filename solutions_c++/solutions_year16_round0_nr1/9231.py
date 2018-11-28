#include <iostream>
using namespace std;

int T;
long long N;
long long ans;

int seen[11];
int totCntSeen;


void chkSeen(long long inp)
{
	while(inp >0){
		int digit = inp%10;
		if(seen[digit] == 0){
			seen[digit] = 1;
			++totCntSeen;
		}
		inp /= 10;
	}
}
long long solve()
{
	totCntSeen=0;
	for(int i=0;i<11;++i){
		seen[i]=0;
	}

	if(N==0){
		return -1;
	}
	
	long long val=0;
	while(totCntSeen != 10){
		val += N;
		chkSeen(val);
		
	}
	return val;
}



int main()
{
	cin>>T;
	for(int xx=1; xx<=T; ++xx){
		cin>>N;
		long long ret = solve();
		if(ret<0){
			cout<<"Case #"<<xx<<": "<<"INSOMNIA"<<endl;
		}
		else{
			cout<<"Case #"<<xx<<": "<<ret<<endl;
		}
	}
	return 0;
}
