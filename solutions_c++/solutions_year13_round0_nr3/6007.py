#include <iostream>
#include <fstream>
using namespace std;

int main() 
{
	fstream in, out;
	in.open("a.txt"); out.open("out.txt"); 
	int ans [] = {1, 4, 9, 121, 484};
	int T = 0, x = 0, A, B;
	int output = 0; 
	in >> T;	
	while(T-- > 0)
	{
		output = 0; 
		in >> A >> B;
		
		for(int i = A ; i <= B; ++i )
			for (int j = 0; j < 5 ; ++j )
				if (ans[j] == i) output++;
		
		x++;
		out << "Case #" << x << ": " << output << endl;
	}
	return 0;
}