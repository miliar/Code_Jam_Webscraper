#include <iostream>
#include <string>
using namespace std;

int main() {
	int i,test_case=10;
	string input;
	cin>>test_case;
	for(i=0;i<test_case;i++)
	{
		cin>>input;
		int len=input.length();
		int count=0;
		for(int j=0; j<len-1;j++)
			{
				if(input[j]!= input[j+1])
				{
					count++;
				}
			}
			if(input[len-1]=='-')
				cout<<"Case #-"<<i+1<<":"<<count+1<<"\n";
			else	
				cout<<"Case #"<<i+1<<":"<<count<<"\n";
	}
	return 0;
}