#include <iostream>
#include <iomanip>
#include <cmath>
#include <vector>
#include <cstring>
#include <map>
#include <bitset>

using namespace std;

int main()
{
	int n;
	cin>>n;
	for(int i=0;i<n;i++)
	{
		int a,b,c;
		cin>>a>>b>>c;
		cout<<"Case #"<<i+1<<": ";
		for(int i=1;i<=a;i++)
			cout<<i<<" ";
		cout<<endl;
	}
}