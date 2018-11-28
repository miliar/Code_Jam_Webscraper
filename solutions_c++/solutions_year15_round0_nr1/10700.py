#include <iostream>
using namespace std;
int test;
int smax;
long long valasz, ossz;
int t[1002];
int main() {
	cin>>test;
	for(int i=1; i<=test; i++)
	{
		cin>>smax;
		for(int j=0; j<=smax; j++)
		{
			char c;
			cin>>c;
			t[j]=c-'0';
		}
		valasz=0;
		ossz=0;
		for(int k=0; k<=smax; k++)
		{
			if(ossz>=k)
			{
				ossz+=t[k];
			}
			else
			{
				valasz+=(k-ossz);
				ossz+=t[k]+(k-ossz);
			}
		}
		cout<<"Case #"<<i<<": "<<valasz<<endl;
	}
	return 0;
}
