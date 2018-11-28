#include <iostream>
#include <string>

using namespace std;




int main() 
{
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) 
	{
		string input = "";
		cin >> input;
		string out = "";

		for( int j = 0; j < input.length(); j++ )
		{
			char next = (input.c_str())[j];
			if(0 == j)
				out += next;
			else
			{
				if( next >= *(out.c_str()) )
					out = next + out;
				else
					out = out + next;
			}
		}
		
		cout << "Case #" << i+1 << ": " << out << endl;
	}

	return 0;
}