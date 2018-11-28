#include<fstream>
using namespace std;
ifstream in("input.txt");
ofstream out("output.txt");
int main()
{
	int T;
	in >> T;
	for(int t=0;t<T;t++)
	{
		double C,F,X;
		in >> C >> F >> X;

		double MIN = X/2.0;
		int a=0;
		double sum=0;
		for(a=1;;a++)
		{
			double b = sum+ (C/(((a-1)*F)+2)) + (X / ((a*F)+2));
			sum = sum + (C/(((a-1)*F)+2));
			if(b < MIN ){
				MIN = b;
			}
			else break;
		}
		out.precision(7);
		out << fixed << "Case #" << t+1 << ": " << MIN << endl;
	}
	return 0;
}