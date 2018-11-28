#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int n,x;
	string y;
	cin>>n;
	for (int i=1;i<=n;i++)
	{
		cin>>x>>y;
		int z=0,a=0;
		for (int j=0;j<y.size();j++)
		{
			if (z<j)
				a++, z++;
			z+=y[j]-'0';
		}
		cout<<"Case #"<<i<<": "<<a<<endl;
	}
	return 0;
}