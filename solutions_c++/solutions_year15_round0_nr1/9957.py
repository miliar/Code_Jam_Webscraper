#include <fstream>
using namespace std;

int main()
{
	int T;
	ifstream in;
	ofstream out;
	in.open("A-small-attempt0.in.txt");
	out.open("output");
	in >> T;

	for(int t = 1;t <= T; t++)
	{
		int smax, result=0, curStand=0;
		string sArray;
		in >> smax;
		in >> sArray;
		for(int i = 0;i <= smax;i ++)
		{
			if(curStand < i)
			{
				result += i - curStand;
				curStand += i - curStand;
			}
			curStand += sArray[i]-'0';
		}
		out << "Case #" << t << ": " << result <<endl;
	}
}