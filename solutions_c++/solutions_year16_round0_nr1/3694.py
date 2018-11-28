#include <iostream>
#include <cstdio>
#include <set>

using namespace std;

int main() 
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T,n; 
	cin>>T;
	for(n=1;n<=T;n++)
	{long long M(0),x; int N,P(0);
	 set<int>D;
	 cin>>N;
	 cout<<"Case #"<<n<<": ";
	 if(N==0)cout<<"INSOMNIA"<<endl; else
	 {
	  while(D.size()<10)
	 {M+=N; x=M;
	  do{
	  	D.insert(x%10);
	  	x/=10;
	  }
	  while(x);
	 }
	 cout<<M<<endl;
	 }
	}
	
	return 0;
}
