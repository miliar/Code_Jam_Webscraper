#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;


int main()
{
	freopen("c:\\1.in","r",stdin);
	freopen("c:\\out1.txt","w",stdout);

	
	int T;
	cin>>T;
	int ii;
	for(ii=1;ii<=T;ii++)
	{
		unsigned long long r,t;
		cin>>r>>t;
		int answer=(sqrt((2*r-1)*(2*r-1)+8*t)-2*r+1)/4;
		cout<<"Case #"<<ii<<": "<<answer<<endl;
    }	
    
return 0;
}

