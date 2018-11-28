/*input
5
0
1
2
11
1692
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
		set<long long> myset;
		long long n;
		cin>>n;
		// cout<<n<<" ";
		if(n)
		{
			bool check = true;
		long long j = 1;
		long long tmp = n*j;
		long long ans,tmp3 ;
		while(check)
		{
			//n*=j;
			tmp = n*j;
			tmp3 = tmp;
			while(tmp)
			{
				long long tmp2 = tmp%10;				
				myset.insert(tmp2);
				tmp = tmp/10;
				// cout<<tmp2<<" ";

			}
			// cout<<endl;
			j++;
			if(myset.size()==10)
			{
				ans = tmp3;
				check = false;
				break;
			}
		}
		cout<<"Case #"<<casen<<": "<<tmp3<<endl;
		}
		else
		{
			cout<<"Case #"<<casen<<": "<<"INSOMNIA"<<endl;
		}

	}
	return 0;
}