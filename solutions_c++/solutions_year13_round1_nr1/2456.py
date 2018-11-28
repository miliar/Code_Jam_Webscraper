#include<cstdio>
#include<iostream>
using namespace std;

long long getarea(long long x)
{
	return (x*1LL*x) - ((x-1)*1LL*(x-1));
}

int main()
{
	long long ans=0;
	int T,tc=1;
	cin >> T;
	while(T--){
	  long long r,t;
	  cin >> r >> t;
	  ans=0;
	  long long curr=r+1;
	  long long num=0,curarea=0;
	  while((curarea + getarea(curr))<=t){
		curarea+=getarea(curr);
		num++;
		curr+=2;
	  }
	  cout <<"Case #"<<tc<<": "<<num<<endl;
	  tc++;
	}
	return 0;
}
