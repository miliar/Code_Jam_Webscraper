#include <iostream>
using namespace std;
int main()
{
	int t,max;
	string str;
	cin>>t;
	for(int j=0;j<t;j++)
	{
		int num =0,fr=0;
		cin>>max>>str;
		for(int i=0;i<max;i++)
		{
			num+=str[i]-'0';
			while(num < (i+1))
			{
				num++;
				fr++;
			}
		}
		cout<<"Case #"<<(j+1)<<": "<<fr<<endl;
	}
}
