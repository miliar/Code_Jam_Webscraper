#include <iostream>
#include <cstdio>

using namespace std;

int main() 
{
	freopen("AL.in","r",stdin);
	freopen("AL.out","w",stdout);
	int N,i,T,ans,D; long long SN,x;
	D=1023;
	cin>>T;
	for(i=1;i<=T;i++)
	{cin>>N;
	 cout<<"Case #"<<i<<": ";
	 int P=0;
	 SN=0;
	 if(N==0)cout<<"INSOMNIA"<<endl; else
	 {
	  while(P<D)
	 {SN+=N; x=SN; ans++;
	  do{
	  	P|=(1<<x%10);
	  	x/=10;
	  }
	  while(x);
	 // cout<<SN<<' '<<ans<<' '<<P<<endl;
	 }
	 cout<<SN<<endl;
	 }
	}
	
	return 0;
}
