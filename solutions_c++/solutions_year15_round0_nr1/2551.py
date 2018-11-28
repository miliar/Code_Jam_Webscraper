#include <iostream>
#include <string>
using namespace std;

int calc()
{
	int sm;string str;
	cin>>sm>>str;
	int sum=0, maxerr=0;
	for(int i=0;i<=sm;i++)
	{
		int tc=str[i]-'0';
		//cerr<<"Status: pos"<<i<<" prevsum"<<sum<<" tc"<<tc<<endl;
		if(tc>0)
		{
			if(i>sum)
			{
				int err=i-sum;
				//cerr<<"ERR:"<<err<<endl;
				if(maxerr<err)maxerr=err;
			}
		}
		sum+=tc;
	}
	return maxerr;
}

int main()
{
	int N;cin>>N;
	for(int i=0;i<N;i++)
		cout<<"Case #"<<(i+1)<<": "<<calc()<<endl;
	return 0;
}