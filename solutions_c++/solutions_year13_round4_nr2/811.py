#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	long long t,te,i,j,k,n,p,x,y;
	ifstream f1;
	ofstream f2;
	f1.open("ai.txt");
	f2.open("ao.txt");
	f1>>t;
	for(te=0;te<t;te++)
	{
		f1>>n>>p;
		i=j=0;
  		if(p==(1<<n))
   			i=j=p-1;
  		else
  		{
		for(k=(1<<n),x=1,y=2;x<p;x+=y,y*=2,j+=k)k/=2;
		k=(1<<(n-1));
		for(x=k,y=2;x<p;)
		{
            i+=y;
            k/=2;x+=k;y*=2;
		}
  		}
		f2<<"Case #"<<(te+1)<<": "<<i<<" "<<j<<"\n";
	}
	return 0;
}
