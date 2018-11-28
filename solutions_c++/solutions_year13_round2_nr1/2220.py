#include<algorithm>
//#include<iostream>
#include<fstream>
using namespace std;

ifstream cin("A-small-attempt2.in");
ofstream cout("out.txt");

int dp[1000005][105],T,N,A;
int motes[100];

int f(int size,int i){
	if(dp[size][i]!=-1) return dp[size][i];
	if(i==N) dp[size][i]=0;
	else{
		if(motes[i]<size) dp[size][i]=f(size+motes[i],i+1);
		else{
			if(size!=1)
				dp[size][i]=min(1+f(size,i+1),1+f(size+size-1,i));
			else
				dp[size][i]=1+f(size,i+1);
		}
	}
	return dp[size][i];
}

int main(){

	cin>>T;
	for(int t=1;t<=T;t++){
		cin>>A>>N;
		for(int i=0;i<N;i++) cin>>motes[i];
		fill(&(dp[0][0]),&(dp[1000004][104])+1,-1);
		sort(&(motes[0]),&(motes[N-1])+1);
		int result=f(A,0);
		cout<<"Case #"<<t<<": "<<result<<endl;
	}
	return 0;
}