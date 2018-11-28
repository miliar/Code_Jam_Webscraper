
#include <iostream>
#include <string>
using namespace std;

int main()
{
	int t;
	cin>>t;
	for( int i = 0 ; i < t ; i++ )
	{
		string input;
		cin>>input;
		char temp = input[0];
		int count=0;
		for(int j = 1; j < input.size() ; j++)
		{
			if( temp == input[j])
				continue;
			if( temp != input[j]  )
			{
				count++;
				temp = input[j];
			}

		}
		if(temp == '-')
			count++;
		cout<<"Case #"<<i+1<<": "<<count<<endl;
	}
	return 0;
}