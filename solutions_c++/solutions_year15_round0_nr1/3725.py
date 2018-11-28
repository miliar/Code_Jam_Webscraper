#include<algorithm>
#include<iostream>
#include<vector>
using namespace std;
int main()
{
	ios_base::sync_with_stdio(false);
	int z;
	cin>>z;
	for(int i=1; i<z+1; i++)
	{
		int n;
		cin>>n;
		string a;
		cin>>a;
		int licznik=a[0]-48;
		int result=0;
		for(int j=1; j<a.size(); j++)
		{
			if(licznik+result<j)
				result+=j-(licznik+result);
			licznik+=a[j]-48;
		}
		cout<<"Case #"<<i<<": "<<result<<endl;
	}
	return 0;
}
