#include<iostream>
#include<cmath>
#include <cstdlib>
#include<fstream>
#include <cstring>
#include<string>
#include<algorithm>
using namespace std;
using std::ifstream;
using std::ofstream;

long long n(long long r, long long t)
{
	long long ans=0;
	long long cal=2*(r+1)-1;
	if((t-=cal)>=0)
	{
		do
		{
			ans++;
			cal+=4;
		}while((t-=cal)>=0);
		return ans;
	}
	else return 0;
}

int main()
{
	ofstream out;
//	out.open("output.txt");
	int T;
	long long r,t;
	cin>>T;
	for(int i=1;i<=T;i++)
	{
		cin>>r>>t;
		cout<<"Case #"<<i<<": "<<n(r,t)<<"\n";
//		out<<"Case #"<<i<<": "<<n(r,t)<<"\n";
	}

//	out.close();

	return(0);
}