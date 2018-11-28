#include <iostream>
#include <fstream>

using namespace std;

int main(int narg, const char** args)
{
	ifstream in(args[1]);
	ofstream out(args[2]);
	int T;
	
	in >> T;
	
	for (int k=0; k<T; ++k)
	{
		int s_max, up = 0, need = 0;
		char* str;
		in >> s_max;
		str = new char[s_max+1];
		in >> str;
		for (int i=0; i<=s_max; ++i)
		{
			if (i <= up)
				up += (str[i]-48);
			else
			{
				need += (i-up);
				up += (i-up) + (str[i]-48);
			}
		}
		out << "Case #" << k+1 << ": " << need << endl;
	}
	
	in.close();
	out.close();
}
