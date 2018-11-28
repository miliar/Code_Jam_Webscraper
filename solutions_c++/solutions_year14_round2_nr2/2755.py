#include <iostream>
#include <algorithm>
#include <vector>
#include <stdio.h>
#include <string.h>

using namespace std;

bool debug=false;

void solve(int c)
{
	long long A,B,K;
	cin>>A>>B>>K;
	long long count=0;
	for(long long i=0;i<A;i++){
		for(long long j=0;j<B;j++){
			if((i&j)<K)
				count++;
		}
	}
	cout<<"Case #"<<c<<": "<<count<<endl;
}

int main(int argc, char** args)
{
	if(argc>1&&args[1][0]=='d'){
		debug=true;
		freopen("sample.in","r",stdin);
	}
	int T;
	cin>>T;
	int c=0;
	while((++c)<=T){
		solve(c);
	}
}

