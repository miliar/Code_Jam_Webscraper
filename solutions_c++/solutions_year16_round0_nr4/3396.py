#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <stack>
using namespace std;
string gen(string x,int Cs,string &Org)
{
	if(Cs==0)return x;
	string next="";
	for(int i=0;i<x.size();++i)
	{
		if(x[i]=='L')
			next+=Org;
		else
			next+=string(Org.size(),'G');
		
	}
	//cout<<next<<endl;
	return gen(next,Cs-1,Org);
}
long long sum(int k,int c)
{
	if(k==1)return 1;
	long long z=1;
	for (int i = 0; i <= c; ++i)
	{
		/* code */
		z=z*k;
	}

	return (1-z)/(1-k)-1;
}
int main(int argc, char const *argv[])
{
	int T,N;
	cin>>T;
	for (int t = 0; t < T; ++t)
	{
		int K,C,S;
		
		string p;
		//cin>>p>>C;
		//K=p.size();
		//p=gen(p,C,p);
		cin>>K>>C>>S;
		long long sumConst=sum(K,C-1);
		//cout<<sumConst<<endl;
		cout<<"Case #"<<t+1<<":";
		for (int i = 0; i < K; ++i)
		{
			/* code */
			long long ind=sumConst*i+i;
			//cout<<p[ind]<<" ";
			cout<<" "<<ind+1;
		}
		cout<<endl;
		//cout<<p[0]<<" "<<p[3*3+3+2]<<endl;
	}
	return 0;
}