/*input
5
2 3 2
1 1 1
2 1 1
2 1 2
3 2 3
*/

#include <iostream>
#include <set>
using namespace std;

int main(int argc, char const *argv[])
{
	int test;
	cin>>test;
	int casen=0;
	while(test--)
	{
		casen++;
		int k,c,s;
		cin>>k>>c>>s;
		if(k!=s)
		{
			cout<<"Case #"<<casen<<": "<<"IMPOSSIBLE"<<endl;
		}
		else
		{
			cout<<"Case #"<<casen<<": ";
			for (int i = 0; i < k; ++i)
			{
				cout<<i+1<<" ";
			}
			cout<<endl;
		}
		
		

	}
	return 0;
}