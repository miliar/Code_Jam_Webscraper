#include <iostream>
#include<fstream>
#include<cstring>
using namespace std;
int main()
{
	
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	long long int test;
	
	cin >> test;
	for(long long int z=0;z<test;z++)
		{
		string n;
	
		cin >> n;
		int i,c=0;
		int l=n.length();
		for(i=l-1;i>=0;i--)
		{
			if(n[i]=='-'&& c%2==0)
			c++;
			else if(n[i]=='+'&& c%2==1)
			c++;
		}
	
	cout<<"Case #"<<(z+1)<<": "<<c<<endl ;
	}
    return 0;
}
