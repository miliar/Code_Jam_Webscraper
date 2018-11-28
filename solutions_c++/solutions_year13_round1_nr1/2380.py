#include<iostream>
#include<cmath>

using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int nc;
	double t,r;
	cin>>nc;
	for(int tc=1;tc<=nc;tc++)
	{
		cin>>r>>t;
		double res=(-2*r+1+sqrt((2*r-1)*(2*r-1)+(8*t)))/4;
		/*double n;
		do{
			n=res;
			res=n-(2*n*n+(2*r-1)*n-t)/(4*n+2*r-1);
		}while(n!=res);*/
		cout<<"Case #"<<tc<<": "<<(int)res<<endl;
	}
	return 0;
}