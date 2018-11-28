#include "iostream"
//#include "bitset"
using namespace std;

int main(int argc, char const *argv[])
{
	int t;
	int counter =1;
	cin>>t;
	while(t--)
	{
		unsigned long long a,b,k,ans=0;
		cin>>a>>b>>k;
		for(unsigned long long i=0;i<k;i++)
		{
			for(unsigned long long j=0;j<a;j++)
			{
				for(unsigned long long m=0;m<b;m++)
				{
					if ((m&j)==i)
						{
							ans++;
						//	cout<<"true"<<" ";
						}/*else
						{
							cout<<"false"<<" ";
						}
					int x=m&j;
					cout<<x<<" ";*/
				}
			}
		}

		cout<<"Case #"<<counter++<<": "<<ans<<endl;
	}
	return 0;
}