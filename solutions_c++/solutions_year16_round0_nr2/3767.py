#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

int main() 
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T,n; 
	cin>>T;
	for(n=1;n<=T;n++)
	{string x; int i,res;
	 cin>>x;
	 cout<<"Case #"<<n<<": ";
	 for(i=res=0;i+1<x.size();i++)
	 	if(x[i]!=x[i+1])res++;
	 res+=x[i]=='-';
	 cout<<res<<endl;
	}
	
	return 0;
}
