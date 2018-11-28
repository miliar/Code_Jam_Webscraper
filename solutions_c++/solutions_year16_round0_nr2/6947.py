
#include <iostream>
#include <vector>
#include <fstream>
#include <string>

using namespace std;

int main()
{

	fstream inp;
	inp.open("input.txt");
	ofstream out;
	out.open("output.txt");
	
	int TestCase;
	string S;
	inp >> TestCase;
	int cas=0;
	while (TestCase--)
	{
		inp >> S;
		cas++;
		char* sub = new char[S.size()];
		int j;
		for (j=0;j<S.size();j++)
			sub[j] = 0;
		int isStop = 1;
		for (int it = 0; it < S.size(); it++)
		{
			if (S[it] == '-'){
				isStop = 0;
			}
			else
				sub[it] = 1;
		}
		int count = 0;
		if (isStop)
			out << "Case #" << cas << ": " << count << endl;
		else{
			for (int it = S.size()-1; it >= 0; it--)
			{
				if (sub[it] == 1)
					continue;
				
				int start = 0;
				while (sub[start] == 1) start++;
				if (start > 0)
				{
					for (int it2 = 0; it2 < start; it2++)
						sub[it2] = 0;
					count++; // one flip 
				}


				for (int it2 = 0; it2 <= it; it2++)
				{
					sub[it2] = 1 - sub[it2];	
				}
				count++;
			}
			out << "Case #" << cas << ": " << count << endl;			
		}

		delete[] sub;
	}

	inp.close();
}
