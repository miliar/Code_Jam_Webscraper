#include <iostream>
using namespace std;

int kejsy;
double target, freq, sumf, cost, prev, sumtime;

double tim_min()
{
	sumf=2;
	prev=0;
	cin >> cost >> freq >> target;
	sumtime=(target/sumf);
	while(1)
	{
		if(sumtime>(prev+(cost/sumf)+(target/(sumf+freq))))
		{
			sumtime=(prev+(cost/sumf)+(target/(sumf+freq)));
			prev+=cost/sumf;
			sumf+=freq;
		}
		else return sumtime;
	}
}

int main ()
{
	cin >> kejsy;
	cout << fixed;
	cout.precision(7);
	for(int i=0; i<kejsy; i++)
	{
		cout << "Case #"<< i+1 << ": "<< tim_min() << endl;
	}
}
