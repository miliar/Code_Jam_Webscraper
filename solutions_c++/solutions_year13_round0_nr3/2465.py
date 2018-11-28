#include <iostream>
#include <vector>
using namespace std;
vector <long long > v;
bool isPalindrome(long long num)
{
	long long temp = num;
	long long rev =0;
	while(temp > 0)
	{
		rev = rev * 10 + temp % 10;
		temp = temp / 10;
	}
	if(rev == num)
		return true;
	return false;
}
int main()
{
	for(long long i = 1 ;i <= 10000000;i++)
		{
			if(isPalindrome(i))
				{
					
					//if(i == 1000001)
						//{
						//	cout<<"YEs"<<"i = "<<i<<endl;

					//long long j = i * i;
					//cout<<"j= "<<j<<endl;
							
						//}
					long long j = i * i;						
					if(isPalindrome(j))
						v.push_back(j);
				}
		}
	//cout<<v.size();
	//for(int i = 0 ;i < v.size();i++)
	//	cout<<v[i]<<" ";
	int test;
	cin>>test;
	int total = 1;
	while(test--)
	{
		long long a,b;
		cin>>a>>b;
		int index1,index2;
		int count = 0;
		for(int i = 0;i < v.size();i++)
			{
				if(v[i] >= a && v[i] <= b)
					count++;
			}
		//cout<<index1<<" "<<index2<<endl;
 		cout<<"Case #"<<total<<": "<<count<<endl;
		//cout<<"Case #"<<total<<": "<<count<<endl;
		total++;
	}
	return 0;
}
