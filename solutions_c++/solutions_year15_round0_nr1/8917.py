#include <cstdio>
#include <iostream>
using namespace std;

int main() {
	int t;
	int r;
	char p[2000];
	scanf("%d",&t);
	for(int T=1;T<=t;++T)
	{
		scanf("%d%s",&r,p);
		int numberofclaps=0;
		int clapse=0;
		for(int i=0;i<=r;++i)
		{

			if(p[i]>'0'&&numberofclaps>=i)
			    numberofclaps+=p[i]-48;
			else if(p[i]>'0')
			    {clapse += i-numberofclaps;
			    numberofclaps=i+p[i]-48;
			    }
			    //if(r==5)
			    //cout<<numberofclaps<<" "<<clapse<<endl;



		}
		cout<<"Case #"<<T<<": "<<clapse<<endl;

	}
	return 0;
}
