#include <iostream>
using namespace std;
int main()
{
	
	int line = 0;
	cin>>line;
	int audience[line];
	for(int i=0;i<line;++i)
	{
		audience[i]=0;
		int shy=0;
		cin>>shy;
		string tmp;
		cin>>tmp;
		int sum=0;
		for(int j=0;j<=shy;++j)
		{	
			while(sum<j)
			{
				audience[i]++;
				sum++;
			}
			sum+=(tmp[j]-'0');
		}
	}

	for(int k=0;k<line;++k)
	{
		cout<<"Case #"<<(k+1)<<": "<<audience[k]<<endl;
	}

}