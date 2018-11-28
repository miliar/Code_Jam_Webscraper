#include <iostream>
#include<set>
using namespace std;

int main() 
{
	int t, index = 1 ;
	long int n, temp, temp2;
	set<int> digits;
	cin>>t;
	
	for(int i=0; i<t; i++)
	{
		cin>>n;
		index = 1;
		digits.clear();
		temp = n;
		temp2 = n;
		if(n == 0)
		cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
		
		else
		{
			while(digits.size() != 10)
			{
				while(temp > 0)
				{
					digits.insert(temp%10);
					temp = temp/10;
				}
				index++;
				temp2 = index*n;
				temp = temp2;
				
			}
			cout<<"Case #"<<i+1<<": "<<temp2-n<<endl;
			
			
		}
		
	}
	return 0;
}