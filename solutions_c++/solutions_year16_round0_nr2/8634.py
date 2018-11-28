#include<iostream>

using namespace std;

int main(){
	
	int test;
	cin>>test;
	
	for(int i = 0; i < test; i++)
	{
		string input;
		cin>>input;
		int totalFlips = 0;

		int j = 1;
		char currentChar = input[0];
		while(input[j] != '\0')
		{
			if(input[j] != currentChar)
			{
				totalFlips++;
				currentChar = input[j];
			}
			
			j++;
		}
		
		if(currentChar == '-')
			totalFlips++;
			
		cout<<"Case #"<<(i+1)<<": "<<totalFlips<<endl;
	}
}
