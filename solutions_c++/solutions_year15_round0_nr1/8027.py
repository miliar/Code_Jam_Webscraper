#include<iostream>
#include<string>
using namespace std;

int input[1001];

int main()
{
	int tc;cin>>tc;
	
	for(int i=0;i<tc;i++)
	{
		//long long result =0;
		int Smax=0;
		cin>>Smax;
		string data;
		cin>>data;
		char * cstr = new char [data.length()+1];
		std::strcpy (cstr, data.c_str());
		input[0] = 0;
		long long count =0;
		for(int j=1;j<=Smax;j++)
		{
			input[j] = input[j-1] + (int) (cstr[j-1] - '0') ;
			if(j > input[j] + count && (cstr[j] != '0'))
			{
				long long diff = j - input[j] - count ;
				count += diff;
			}
		}

		cout<<"Case #"<<i+1<<": "<<count<<"\n";
	}

	return 0;
}