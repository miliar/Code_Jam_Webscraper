#include<iostream>
#include<cmath>
#include <cstdlib>
using namespace std;
using std::ifstream;
using std::ofstream;

long long answer(long long m, long long g)
{
	long long ans=0;
	long long cal=2*(m+1)-1;
	if((g-=cal)>=0)
	{
		do
		{
			ans++;
			cal+=4;
		}while((g-=cal)>=0);
		return ans;
	}
	else return 0;
}

int main()
{

	int T;
	long long r,t;
	cin>>T;
	for(int i=1;i<=T;i++)
	{
		cin>>r>>t;
		cout<<"Case #"<<i<<": "<<answer(r,t)<<"\n";
	}

//	out.close();

	return(0);
}