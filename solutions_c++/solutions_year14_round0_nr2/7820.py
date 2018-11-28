#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	ifstream in ("B-large.in");
	ofstream out ("ans.txt");
	out.setf(ios::fixed, ios::floatfield);
	int t, iter;
	double prev, buytime, next, cost, produce, goal, rate;
	in >> t;
	for (iter = 0; iter < t; iter ++)
	{
		in >> cost >> produce >> goal;
		rate = 2;
		buytime = cost / rate;
		next = 0;
		prev = goal / rate;
		do
		{
			if (next)
			{
				prev = next;
				next -= goal / rate;
			}
			rate += produce;
			next += buytime + (goal / rate);
			buytime = cost / rate;
		} while (next < prev);
		out<<"Case #"<<iter+1<<": "<<prev<<endl;
	}
	return 0;
}