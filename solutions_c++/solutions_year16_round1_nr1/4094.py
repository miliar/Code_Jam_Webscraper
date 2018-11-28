#include <iostream>

using namespace std;

int main()
{
	int T; cin>>T;

	for(int i = 0; i < T; i++)
	{
		string input; cin>>input;
		string answer="";

		answer = input[0];

		for(int j = 1; j < input.length(); j++)
		{
			if(input[j] >= answer[0])
				answer = input[j] + answer;
			else
				answer = answer + input[j];
		}

		cout<<"Case #"<<(i+1)<<": "<<answer<<endl;
	}
}